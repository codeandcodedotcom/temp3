import json
import random

# Load questions from JSON
with open("questions.json", "r") as f:
    questionnaire = json.load(f)

total_score = 0

for i, q in enumerate(questionnaire, start=1):
    print(f"\nQ{i}: {q['question']}")

    # Print all options
    for j, opt in enumerate(q["options"], start=1):
        label = opt.get("label", j)  # fallback index if no label
        print(f"  {label}. {opt['text']}")

    # Randomly choose an option
    chosen = random.choice(q["options"])
    chosen_text = chosen["text"]
    chosen_score = chosen.get("label", 0)  # 0 if no score

    # Add to total
    total_score += chosen_score

    # Print chosen option
    print(f"👉 Chosen: {chosen_text} (Score: {chosen_score})")

# At the end, print total score
print("\n===========================")
print(f"Total Score: {total_score}")
print("===========================")
