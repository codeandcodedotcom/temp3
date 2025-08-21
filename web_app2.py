import re
import time
import streamlit as st
from main3 import (
    load_questions,
    run_questionnaire,
    interpret_score,
    load_text_as_documents,
    build_or_load_vector_store,
    retrieve_context_per_question,
    build_prompt,
    call_llm,
    QUESTIONS_FILE,
    PAR_FILE,
    PILM_FILE,
    PAR_VS_DIR,
    PILM_VS_DIR,
    PER_QUESTION_K,
)

st.set_page_config(page_title="Project Brief Generator", page_icon="📝", layout="centered")
st.title("📝 Project Brief Generator")
# st.caption("Questionnaire → Score → (optional) PAR/PILM per-question retrieval → LLM brief")

# with st.sidebar:
#     st.subheader("Run Settings")
#     typing_speed = st.slider("Typing speed (seconds per line)", 0.0, 0.2, 0.02, 0.01)
#     st.caption("Lower = faster typing effect")
#     st.divider()
#     st.caption("Each run randomly selects questionnaire options.")

typing_speed = 0.01

def type_out(text, container, delay=0.01):
    """Simulate typing effect character by character."""
    out = ""
    for char in text:
        out += char
        container.markdown(out)
        time.sleep(delay)

# # ---------- 1) Sanitize: make headings clean, split inline headings ----------
# HEADINGS = ["Project Name", "Project Sponsor", "Project Description", "Risks", "Assumptions", "Benefits"]
# HEADINGS_RE = r"(Project Name|Project Sponsor|Project Description|Risks|Assumptions|Benefits)"

# def sanitize_output(text):
#     # Drop any preface before first heading
#     m = re.search(rf"(?mi)^{HEADINGS_RE}\s*$", text)
#     if m:
#         text = text[m.start():]

#     # Normalize fancy bullets to '- ' for easier parsing later
#     text = re.sub(r"^[\s•·▪●]+\s*", "- ", text, flags=re.MULTILINE)

#     # Split lines where a heading and content are on the same line:
#     #   "Project Name: Foo"  -> "Project Name\nFoo"
#     text = re.sub(
#         rf"(?im)^\s*(?:- )?\s*{HEADINGS_RE}\s*[:\-]?\s+(.*)$",
#         lambda m: f"{m.group(1)}\n{m.group(2).strip()}",
#         text,
#     )
#     return text.strip()

# Parse into sections robustly
def parse_sections(text):
    sections = {h: [] for h in HEADINGS}
    current = None

    for raw in text.splitlines():
        line = raw.rstrip()
        if not line.strip():
            continue

        # Heading on its own line
        if re.fullmatch(rf"(?i){HEADINGS_RE}", line.strip()):
            current = line.strip().title()  # normalise case (e.g., Project Name)
            continue

        if current is None:
            # ignore stray content before first heading
            continue

        if current in ["Risks", "Assumptions", "Benefits"]:
            # Treat as bullet line; strip leading "- " if present
            line = re.sub(r"^\s*-\s*", "", line).strip()
            if line:
                sections[current].append(line)
        else:
            # Non-list sections -> accumulate plain text lines
            sections[current].append(line)

    # Join non-list sections into one paragraph
    for key in ["Project Name", "Project Sponsor", "Project Description"]:
        sections[key] = " ".join(sections[key]).strip()

    # Ensure lists exist (avoid None)
    for key in ["Risks", "Assumptions", "Benefits"]:
        sections[key] = [x for x in sections[key] if x]

    return sections

# Format to Markdown with bold headers, blank lines, bullets
def format_sections_to_markdown(s):
    parts = []

    def add_block(title, body, force_newline=False):
        parts.append(f"**{title}**")
        if force_newline:
            parts.append("")  # extra newline between header and body

        if isinstance(body, list):
            if body:
                parts.extend([f"- {item}" for item in body])
            else:
                parts.append("- (none provided)")
        else:
            parts.append(body if body else "(not provided)")

        parts.append("")  # blank line after every section

    # These three should have newline between header and body
    add_block("Project Name", s.get("Project Name", ""), force_newline=True)
    add_block("Project Sponsor", s.get("Project Sponsor", ""), force_newline=True)
    add_block("Project Description", s.get("Project Description", ""), force_newline=True)

    # Lists
    add_block("Risks", s.get("Risks", []))
    add_block("Assumptions", s.get("Assumptions", []))
    add_block("Benefits", s.get("Benefits", []))

    return "\n".join(parts).strip() + "\n"

# Run button 
run_btn = st.button("Generate Project Brief")

if run_btn:
    status = st.empty()
    status.info("Loading questionnaire and running simulation...")

    # Questionnaire
    questions = load_questions(QUESTIONS_FILE)
    responses, total_score, product_answer = run_questionnaire(questions)

    # Assessment
    assessment = interpret_score(total_score)

    # Context selection (per-question retrieval)
    context_text = None
    ref_doc_label = "NONE"

    if total_score < 40:
        status.warning("Score < 40 -> Using Questionnaire + Assessment only (no PILM or PAR).")
    else:
        pa = (product_answer or "").strip().lower()
        if pa == "no":
            status.info("Score >= 40 and Product = No -> Using PAR context.")
            ref_doc_label = "PAR"
            par_docs = load_text_as_documents(PAR_FILE)
            par_vs = build_or_load_vector_store(par_docs, PAR_VS_DIR)
            context_text = retrieve_context_per_question(par_vs, responses, per_q_k=PER_QUESTION_K)
        elif pa == "yes":
            status.info("Score >= 40 and Product = Yes -> Using PILM context.")
            ref_doc_label = "PILM"
            pilm_docs = load_text_as_documents(PILM_FILE)
            pilm_vs = build_or_load_vector_store(pilm_docs, PILM_VS_DIR)
            context_text = retrieve_context_per_question(pilm_vs, responses, per_q_k=PER_QUESTION_K)
        else:
            status.warning("Product-related answer missing/unknown; proceeding without document context.")
            ref_doc_label = "UNKNOWN"

    # Build prompt -> LLM
    st.markdown(f"**Reference document:** `{ref_doc_label}`")
    status.info("Calling the model...")
    prompt = build_prompt(responses, assessment, context_text)
    raw = call_llm(prompt)

    # clean = sanitize_output(raw)
    # sections = parse_sections(clean)
    sections = parse_sections(raw)
    md = format_sections_to_markdown(sections)

    status.success("Model generated the project brief")
    st.divider()
    st.subheader("Generated Project Brief")
    placeholder = st.empty()
    type_out(md, placeholder, delay=typing_speed)
    st.toast("Done!", icon="✅")


    with st.expander("Debug details"):
        st.write("**Total Score:**", total_score)
        st.write("**Project Product Related:**", product_answer)
        st.write("**Assessment:**", assessment)
        st.write("**Q&A:**", responses)
        # if context_text:
        #     st.write("**Context (first 1000 chars):**")
        #     st.code(context_text[:1000])

else:
    st.info("Click **Generate Project Brief** to run.")
