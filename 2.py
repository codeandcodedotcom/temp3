from openai import OpenAI

client = OpenAI(api_key="your_api_key_here")

def generate_project_brief(chosen_answers, assessment):
    # Format questionnaire responses nicely
    responses_text = "\n".join([
        f"- {ans['question']}\n  👉 {ans['chosen_option']} (Score: {ans['score']})"
        for ans in chosen_answers
    ])

    prompt = f"""
You are a project management assistant.
Based on the questionnaire responses and assessment, generate a structured project brief.

Format strictly as:

Project Name: <fill a name>
Project Sponsor: <use the given sponsor name>
Project Description: <short description>
Risks: <bullet list>
Assumptions: <bullet list>
Benefits: <bullet list>

Questionnaire Responses:
{responses_text}

Assessment:
Complexity: {assessment['complexity']}
Recommendation: {assessment['recommendation']}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",   # or whichever LLM you are using
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content


def main():
    questions = load_questions()
    total_score, chosen_answers = run_questionnaire(questions)

    print("\n" + "="*50)
    print(f"✅ Total Score: {total_score}")

    assessment = interpret_score(total_score)
    print(f"📊 Complexity Level: {assessment['complexity']}")
    print(f"📌 Recommendation: {assessment['recommendation']}")
    print("="*50)

    # 🔹 Pass to LLM
    project_brief = generate_project_brief(chosen_answers, assessment)
    print("\n📄 Generated Project Brief:")
    print(project_brief)


if __name__ == "__main__":
    main()
