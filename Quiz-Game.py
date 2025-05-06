import json
import random

with open("questions.json", "r", encoding="utf-8") as file:
    quiz = json.load(file)

random.shuffle(quiz)


score = 0  # αρχικό σκορ

print("Καλώς ήρθες στο Quiz Γνώσεων!\n")

for index, q in enumerate(quiz):
    print(f"Ερώτηση {index + 1}: {q['question']}")
    
    for option in q['options']:
        print(option)

    answer = input("Η απάντησή σου (Α, Β, Γ, Δ): ").strip().upper()

    if answer == q['answer']:
        print("✅ Σωστά!\n")
        score += 1
    else:
        print(f"❌ Λάθος. Η σωστή απάντηση ήταν: {q['answer']}\n")

print(f"Τελικό σκορ: {score}/{len(quiz)}")

