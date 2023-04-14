import json

with open('questions.json', 'r') as f:
    questions = json.load(f)

score = 0
total_questions = len(questions)

for i, question in enumerate(questions):
    print(f'Question {i+1}/{total_questions}: {question["question"]}')
    for j, answer in enumerate(question['answers']):
        print(f'{j+1}. {answer}')

    while True:
        user_answer = input('Enter the correct answer number: ')
        if not user_answer.isdigit():
            print('Invalid input. Please enter a number.')
            continue
        user_answer = int(user_answer)
        if user_answer < 1 or user_answer > len(question['answers']):
            print(f'Invalid input. Please enter a number between 1 and {len(question["answers"])}')
            continue
        if question['answers'][user_answer-1] == question['correct_answer']:
            print('Correct answer!')
            score += 1
            break
        else:
            print('Incorrect answer.')
            break

print(f'You scored {score}/{total_questions}')
