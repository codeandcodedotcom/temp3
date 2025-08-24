import os
import json
import random
from typing import Tuple, Dict, List, Optional
from dotenv import load_dotenv
from openai import OpenAI
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from config import (
    API_KEY,
    BASE_URL,
    VECTORSTORE_PATH,
    EMBEDDING_MODEL,
    GENERATION_MODEL,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    TOP_K,         
    TEMPERATURE,
    MAX_TOKENS,
    PER_QUESTION_K
)
from mocks import MOCK_CASES

USE_MOCKS = True  # ← turn ON for demo (no LLM calls). Set to False to use real LLM later.

# import config as _cfg
# PER_QUESTION_K = getattr(_cfg, "PER_QUESTION_K", 1)

PRODUCT_Q_TEXT = "Is your project Product Related?"
QUESTIONS_FILE = "questions.json"
PAR_FILE = "PAR.txt"
PILM_FILE = "PILM.txt"

# two separate cache folders underneath VECTORSTORE_PATH
PAR_VS_DIR  = os.path.join(VECTORSTORE_PATH, "par")
PILM_VS_DIR = os.path.join(VECTORSTORE_PATH, "pilm")

SPONSORS = ["Alice Johnson", "Robert Martinez", "Priya Desai", "John Smith", "Fatima Sayed"]

load_dotenv()
client   = OpenAI(api_key=API_KEY, base_url=BASE_URL)

model_id = EMBEDDING_MODEL if "/" in EMBEDDING_MODEL else f"sentence-transformers/{EMBEDDING_MODEL}"
embedder = HuggingFaceEmbeddings(model_name=model_id)


def get_random_sponsor():
    return random.choice(SPONSORS)

def load_questions(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def choose_option_randomly(question):
    chosen = random.choice(question["options"])
    return chosen["text"], int(chosen.get("score", 0))

def run_questionnaire(questions):
    """
    Prints each question and options, randomly picks an option, tracks total score.
    Returns (responses map, total_score, product_related_answer 'Yes'/'No'/None)
    """
    total_score = 0
    responses = {}
    product_answer: Optional[str] = None

    for i, q in enumerate(questions, start=1):
        print(f"\nQ{i}: {q['question']}")
        for j, opt in enumerate(q["options"], start=1):
            # s = f" (Score: {opt['score']})" if "score" in opt else ""
            print(f"  {j}. {opt['text']}")

        chosen_text, chosen_score = choose_option_randomly(q)
        responses[q["question"]] = chosen_text
        total_score += chosen_score
        print(f" Chosen: {chosen_text}")

        if q["question"].strip().lower() == PRODUCT_Q_TEXT.strip().lower():
            product_answer = chosen_text.strip()

    print("\n==============================")
    print(f"Total Score: {total_score}")
    print("==============================")
    return responses, total_score, product_answer


def interpret_score(total_score):
    if 1 <= total_score <= 27:
        return {
            "complexity": "Low Complexity / Standard execution",
            "recommendation": (
                "At this stage, the project does not require the support of a dedicated "
                "Project Management (PM) professional. Please reach out to your division PMO "
                "for guidance, support, and training recommendations as needed."
            ),
        }
    elif 28 <= total_score <= 39:
        return {
            "complexity": "Medium Complexity / Focus on risk",
            "recommendation": (
                "Based on the assessment, this project could be assigned a Project Lead. "
                "A Project Lead could provide the necessary oversight and direction to ensure successful delivery."
            ),
        }
    elif 40 <= total_score <= 51:
        return {
            "complexity": "High Complexity / Need active governance",
            "recommendation": (
                "The assessment indicates that this project should be managed by a Project Manager. "
                "Assigning a Project Manager will help ensure effective planning, execution, and control "
                "throughout the project lifecycle."
            ),
        }
    elif 52 <= total_score <= 60:
        return {
            "complexity": "Critical Complexity / Need active governance",
            "recommendation": (
                "The assessment suggests that this initiative is best classified as a Programme. "
                "It should be supported by a team of PM professionals, providing comprehensive programme "
                "management to coordinate multiple related projects and achieve strategic objectives."
            ),
        }
    return {"complexity": "Invalid Score", "recommendation": "Score out of expected range."}


def load_text_as_documents(path):
    loader = TextLoader(path, encoding="utf-8")
    docs = loader.load()
    blocks = [d.page_content for d in docs if d.page_content.strip()]
    return [Document(page_content=b) for b in blocks]

def chunk_documents(documents):
    splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    return splitter.split_documents(documents)

def _has_faiss_index(dir_path):
    return os.path.exists(os.path.join(dir_path, "index.faiss")) and \
           os.path.exists(os.path.join(dir_path, "index.pkl"))

def build_or_load_vector_store(documents, dir_path):
    os.makedirs(dir_path, exist_ok=True)
    if _has_faiss_index(dir_path):
        return FAISS.load_local(dir_path, embedder, allow_dangerous_deserialization=True)
    chunks = chunk_documents(documents)
    vs = FAISS.from_documents(chunks, embedder)
    vs.save_local(dir_path)
    return vs

# per-question retrieval 
def build_query_for_question(q, a):
    # keep it simple and focused; helps MMR/semantic match
    return f"Question: {q}\nAnswer: {a}\nFocus: scope, risks, assumptions, governance, benefits, delivery approach."

def retrieve_context_per_question(vs, responses, per_q_k = 1):
    # Use MMR for diversity; fall back to similarity if MMR unsupported
    retriever = vs.as_retriever(
        search_type="mmr",
        search_kwargs={"k": per_q_k, "fetch_k": max(40, per_q_k * 8), "lambda_mult": 0.3},
    )
    seen = set()
    gathered = []

    for q, a in responses.items():
        query = build_query_for_question(q, a)
        docs = retriever.get_relevant_documents(query)
        for d in docs:
            text = d.page_content.strip()
            if text and text not in seen:
                seen.add(text)
                gathered.append(text)

    return "\n\n".join(gathered)


def build_prompt(responses, assessment, context):
    sponsor = get_random_sponsor()
    formatted_responses = "\n".join([f"- {q}\n  {a}" for q, a in responses.items()])
    context_block = context if context else "(no additional context provided)"

    return f"""
        You are a project management assistant.
        Generate a structured project brief based on the following questionnaire responses, assessment and context. Use UK English.
        Return ONLY the sections below, exactly in this order, with these exact headings.
        Each heading must be on its own line with NO bullet / NO colon.
        Immediately after the heading, put the content on the NEXT line.
        Use '-' bullets ONLY inside Risks, Assumptions, Benefits lists.
        Do not add any preface or trailer text. Use UK English.
        Keep 'Project Description' under 120 words.


        Project Name
        <name>

        Project Sponsor
        {sponsor}

        Project Description
        <The project description must be within 120 words.>

        Risks
        <bullet list>

        Assumptions
        <bullet list>

        Benefits
        <bullet list>


        Questionnaire Responses:
        {formatted_responses}

        Assessment:
        Complexity: {assessment['complexity']}
        Recommendation: {assessment['recommendation']}

        Context:
        {context_block}
        """.strip()


def call_llm(prompt):
    resp = client.chat.completions.create(
        model=GENERATION_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=TEMPERATURE,
        # max_tokens=MAX_TOKENS,
    )
    return resp.choices[0].message.content.strip()


def main():
    # Load questionnaire
    questions = load_questions(QUESTIONS_FILE)

    if USE_MOCKS:
        # ---- DEMO: pick one pre-defined brief and matching responses ----
        case = random.choice(MOCK_CASES)
        responses = case["responses"]
        total_score = case["total_score"]
        product_answer = case["product_answer"]

        # Print to terminal (so you see backend output)
        print("\n[DEMO MODE] Using mock case:", case["id"])
        print("Product Related:", product_answer, "| Total Score:", total_score)

        # Create a CLI-friendly render of the sections
        s = case["sections"]
        print("\n================ PROJECT BRIEF (MOCK) ================\n")
        print("Project Name\n", s.get("Project Name",""), "\n", sep="")
        print("Project Sponsor\n", s.get("Project Sponsor",""), "\n", sep="")
        print("Project Description\n", s.get("Project Description",""), "\n", sep="")
        print("Risks")
        for r in s.get("Risks", []): print("-", r)
        print("\nAssumptions")
        for a in s.get("Assumptions", []): print("-", a)
        print("\nBenefits")
        for b in s.get("Benefits", []): print("-", b)
        print("\n======================================================\n")
        return

    # Run questionnaire -> collect answers + score + product flag
    responses, total_score, product_answer = run_questionnaire(questions)

    assessment = interpret_score(total_score)

    context_text = None

    if total_score < 40:
        print("Score < 40 -> no retrieval. Using Questionnaire + Assessment only.")
        print("Reference doc: NONE (below threshold)")
    else:
        pa = (product_answer or "").strip().lower()
        if pa == "no":
            print("Score >= 40 and Product = No -> using PAR vector store (per-question retrieval).")
            print("Reference doc: PAR")
            par_docs = load_text_as_documents(PAR_FILE)
            par_vs = build_or_load_vector_store(par_docs, PAR_VS_DIR)
            context_text = retrieve_context_per_question(par_vs, responses, per_q_k=PER_QUESTION_K)
        elif pa == "yes":
            print("Score >= 40 and Product = Yes -> using PILM vector store (per-question retrieval).")
            print("Reference doc: PILM")
            pilm_docs = load_text_as_documents(PILM_FILE)
            pilm_vs = build_or_load_vector_store(pilm_docs, PILM_VS_DIR)
            context_text = retrieve_context_per_question(pilm_vs, responses, per_q_k=PER_QUESTION_K)
        else:
            print("Product-related answer missing/unknown; proceeding without vector context.")
            print("Reference doc: UNKNOWN")

    # Build prompt & call the model
    prompt = build_prompt(responses, assessment, context_text)
    print("\nModel is generating project brief...")
    output = call_llm(prompt)

    print("\n================ PROJECT BRIEF ================\n")
    print(output)
    print("\n===============================================\n")

if __name__ == "__main__":
    main()
