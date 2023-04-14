# Python Quiz

This is a simple command-line application that allows the user to take a quiz with multiple questions. The questions are randomly shuffled, and the user is prompted to select the correct answer from a list of possible answers.

## Requirements

The application requires Python 3.x.

## Usage

1. Clone the repository or download and extract the archive.
2. Open a command prompt or terminal and navigate to the directory where the main.py file is located.
3. Run the program by typing python main.py in the command prompt or terminal.
4. Take the quiz by selecting the number of the answer and pressing Enter. If an invalid answer number is entered, the user will be prompted to enter the answer again.
5. After finishing the quiz, the user's score will be displayed.

## jSON Format

The questions are stored in a JSON file with the following format:

```json
{
    "questions": [
        {
            "text": "What is the capital of France?",
            "options": ["London", "Paris", "Berlin", "Madrid"],
            "answer": "Paris"
        },
        {
            "text": "What is the largest planet in our solar system?",
            "options": ["Mars", "Jupiter", "Saturn", "Neptune"],
            "answer": "Jupiter"
        },
        ...
    ]
}
```
The "questions" key contains an array of question objects. Each question object has the following keys:
* "text": the text of the question.
* "options": an array of possible answer options.
* "answer": the correct answer in the "options" array.

## License

This program is available under the MIT License.
