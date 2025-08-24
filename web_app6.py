import re
import time
import random
import streamlit as st
from mocks import MOCK_CASES
import streamlit.components.v1 as components
from main4 import (
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


USE_MOCKS = True


st.set_page_config(page_title="Project Brief Generator", page_icon="📝", layout="centered")
st.title("📝 Project Brief Generator")

typing_speed = 0.01

def type_out(text, container, delay=0.01):
    """Simulate typing effect character by character."""
    out = ""
    for char in text:
        out += char
        container.markdown(out)
        time.sleep(delay)

HEADINGS = ["Project Name", "Project Sponsor", "Project Description", "Risks", "Assumptions", "Benefits"]
HEADINGS_RE = r"(Project Name|Project Sponsor|Project Description|Risks|Assumptions|Benefits)"

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


def render_questionnaire_block(questions, responses):
    """
    Shows each question with numbered options and the chosen answer.
    """
    import textwrap

    for i, q in enumerate(questions, start=1):
        st.markdown(f"**Q{i}: {q['question']}**")

        # Build numbered options
        lines = []
        for idx, opt in enumerate(q.get("options", []), start=1):
            line = f"{idx}. {opt.get('text','')}"
            # if "score" in opt:
            #     line += f" (Score: {opt['score']})"
            lines.append(line)

        if lines:
            st.code("\n".join(lines))

        # Chosen answer
        chosen = responses.get(q["question"], "(not answered)")
        st.markdown(f"**Chosen:** {chosen}")
        st.markdown("---")


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

    return "\n".join(parts).strip()
    # return "\n".join(parts).strip() + "\n"

# run_btn = st.button("Generate Project Brief")

questions = load_questions(QUESTIONS_FILE)
# responses, total_score, product_answer = run_questionnaire(questions)
# assessment = interpret_score(total_score)

if USE_MOCKS:
    ss = st.session_state
    ss.setdefault("show_brief", False)
    ss.setdefault("jumped", False)
    ss.setdefault("ref_doc_label", "NONE")
    ss.setdefault("current_case", None)   # NEW

    # pick once and keep the same case across reruns
    if ss.current_case is None:
        ss.current_case = random.choice(MOCK_CASES)

    case = ss.current_case
    responses = case["responses"]
    total_score = case["total_score"]
    product_answer = case["product_answer"]
    sections = case["sections"]
    md = format_sections_to_markdown(sections)
    ref_doc_label = ("PILM" if product_answer.lower()=="yes" and total_score>=40
                        else "PAR" if product_answer.lower()=="no" and total_score>=40
                        else "NONE")
    assessment = interpret_score(total_score)

    ss.ref_doc_label = ref_doc_label

    st.divider()

    # ss = st.session_state
    # ss.setdefault("show_brief", False) 
    # ss.setdefault("jumped", False) 
    # ss.ref_doc_label = ref_doc_label

    if "show_brief" not in ss:
        ss.show_brief = False

    tab1, tab2 = st.tabs(["Questionnaire", "Project Brief"])

    # Auto-jump to the "Project Brief" tab (2nd tab) after user clicks the button
    if ss.show_brief and not ss.jumped:
        ss.jumped = True
        components.html(
            """
            <script>
            // give Streamlit a beat to render the tabs
            setTimeout(() => {
                const tabs = window.parent.document.querySelectorAll('button[role="tab"]');
                if (tabs && tabs[1]) { tabs[1].click(); }
            }, 60);
            </script>
            """,
            height=0,
        )


    with tab1:
        st.subheader("Questionnaire")
        status_t1 = st.empty()
        status_t1.info("Loading questionnaire...")
        questions = load_questions(QUESTIONS_FILE)
        render_questionnaire_block(questions, responses)
        ref_doc_label = st.session_state.get("ref_doc_label", "NONE")

        st.markdown(f"**Total Score:** {total_score}")
        status_t1.success(f"Questionnaire loaded.")
        # st.markdown(f"**Project Product Related:** {product_answer}")
        # st.markdown(f"**Reference document:** `{ref_doc_label}`")
        # st.toast("Done!", icon="✅")
        # run_btn = st.button("Generate Project Brief", key="gen_btn_mock")

        if st.button("Generate Project Brief", key="gen_btn_mock"):
            ss.md = md          # store the exact brief content for this case
            ss.show_brief = True
            ss.jumped = False           # allow the auto-switch
            st.rerun()

    with tab2:
        st.subheader("Project Brief")
        status_t2 = st.empty()
        status_t2.info(f"Score: {total_score} -> Product: {product_answer} -> Referring {ss.ref_doc_label}")
        status_t2.info("Generating project brief...")
        if ss.show_brief:
            st.markdown(f"**Reference document:** `{ss.ref_doc_label}`")
            st.divider()
            placeholder = st.empty()
            type_out(ss.md, placeholder, delay=typing_speed)
            st.toast("Done!", icon="✅")
            status_t2.success("Project brief generated")
        else:
            st.info("Click **Generate Project Brief** in the Questionnaire tab to proceed.")

        with st.expander("Debug details"):
            st.write("**Total Score:**", total_score)
            st.write("**Project Product Related:**", product_answer)
            st.write(f"**Reference document:** `{ref_doc_label}`")
            st.write("**Assessment:**", assessment)
            st.write("**Q&A:**", responses)

else:
    # -----------------------
    # LLM MODE (real run)
    # -----------------------
    ss = st.session_state
    ss.setdefault("show_brief", False)
    ss.setdefault("jumped", False)
    ss.setdefault("ref_doc_label", "NONE")
    ss.setdefault("md", "")

    # Load questions once and keep simulated responses stable across reruns
    questions = load_questions(QUESTIONS_FILE)
    if "responses_real" not in ss:
        responses, total_score, product_answer = run_questionnaire(questions)
        assessment = interpret_score(total_score)
        ss.responses_real = responses
        ss.total_score_real = total_score
        ss.product_answer_real = product_answer
        ss.assessment_real = assessment
    else:
        responses = ss.responses_real
        total_score = ss.total_score_real
        product_answer = ss.product_answer_real
        assessment = ss.assessment_real

    # Tabs stay in fixed order
    tab1, tab2 = st.tabs(["Questionnaire", "Project Brief"])

    # After button click, auto-jump to tab 2 by programmatically clicking it
    if ss.show_brief and not ss.jumped:
        ss.jumped = True
        components.html(
            """
            <script>
            setTimeout(() => {
              const tabs = window.parent.document.querySelectorAll('button[role="tab"]');
              if (tabs && tabs[1]) { tabs[1].click(); }
            }, 60);
            </script>
            """,
            height=0,
        )

    with tab1:
        st.subheader("Questionnaire")
        status_t1 = st.empty()
        status_t1.info("📋 Please review the questionnaire and click Generate when ready.")

        render_questionnaire_block(questions, responses)
        st.markdown(f"**Total Score:** {total_score}")
        st.markdown(f"**Project Product Related:** {product_answer}")
        status_t1.success("✅ Questionnaire loaded.")

        if st.button("Generate Project Brief", key="gen_btn_real"):
            ctx = None
            ref = "NONE"
            if total_score >= 40:
                pa = (product_answer or "").strip().lower()
                if pa == "no":
                    ref = "PAR"
                    par_docs = load_text_as_documents(PAR_FILE)
                    par_vs = build_or_load_vector_store(par_docs, PAR_VS_DIR)
                    ctx = retrieve_context_per_question(par_vs, responses, per_q_k=PER_QUESTION_K)
                elif pa == "yes":
                    ref = "PILM"
                    pilm_docs = load_text_as_documents(PILM_FILE)
                    pilm_vs = build_or_load_vector_store(pilm_docs, PILM_VS_DIR)
                    ctx = retrieve_context_per_question(pilm_vs, responses, per_q_k=PER_QUESTION_K)
                else:
                    ref = "UNKNOWN"

            ss.ref_doc_label = ref

            status_t1.info("⏳ Calling the model...")
            prompt = build_prompt(responses, assessment, ctx)
            raw = call_llm(prompt)
            sections = parse_sections(raw)
            ss.md = format_sections_to_markdown(sections)
            status_t1.success("✅ Project brief generated.")

            ss.show_brief = True
            ss.jumped = False
            st.rerun()

    with tab2:
        st.subheader("Project Brief")
        status_t2 = st.empty()
        status_t2.info(f"Score: {total_score} -> Product: {product_answer} -> Referring {ss.ref_doc_label}")

        if ss.show_brief:
            status_t2.info("✍️ Generating project brief...")
            st.markdown(f"**Reference document:** `{ss.ref_doc_label}`")
            st.divider()
            placeholder = st.empty()
            type_out(ss.md, placeholder, delay=typing_speed)
            st.toast("Done!", icon="✅")
            status_t2.success("✅ Project brief generated.")
        else:
            status_t2.info("ℹ️ Click Generate Project Brief in the Questionnaire tab to proceed.")

        with st.expander("Debug details"):
            st.write("**Total Score:**", total_score)
            st.write("**Project Product Related:**", product_answer)
            st.write("**Reference document:**", ss.ref_doc_label)
            st.write("**Assessment:**", assessment)
            st.write("**Q&A:**", responses)
