import random

questions = [
    {
        "question": "What is the capital of France?",
        "answers": ["Paris", "London", "Berlin", "Madrid"]
    },
    {
        "question": "What is the largest country in the world?",
        "answers": ["Russia", "China", "USA", "Canada"]
    },
    {
        "question": "What is the currency of Japan?",
        "answers": ["Yen", "Dollar", "Euro", "Pound"]
    }
]

random.shuffle(questions)  # losowe ustawienie pytań

score = 0  # wynik użytkownika

for q in questions:
    print(q["question"])
    for i, a in enumerate(q["answers"]):
        print(f"{i + 1}. {a}")
    user_answer_valid = False
    while not user_answer_valid:
        user_answer = input("Enter the number of your answer: ")
        if not user_answer.isdigit() or int(user_answer) < 1 or int(user_answer) > len(q["answers"]):
            print("Invalid answer! Please choose a valid answer number.")
        elif q["answers"][int(user_answer) - 1] == q["answers"][0]:
            print("Correct answer!")
            score += 1
            user_answer_valid = True
        else:
            print("Wrong answer! Please try again.")

print(f"Your score: {score} out of {len(questions)}")

print("Your score is " + str(score) + " out of " + str(len(questions)) + " possible points.")
