def ask_question(question, choices, correct_answer):
    """Ask a question and check the user's answer."""
    print(question)
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")

    try:
        answer = int(input("Choose the number of your answer: "))
        if 1 <= answer <= len(choices):
            if choices[answer - 1] == correct_answer:
                return True
            else:
                return False
        else:
            print("Invalid choice. Please choose a valid option.")
            return False
    except ValueError:
        print("Invalid input. Please enter a number.")
        return False

def main():
    """Main function to run the quiz game."""
    questions = [
        {
            'question': "What is the capital of France?",
            'choices': ["Berlin", "Madrid", "Paris", "Rome"],
            'correct_answer': "Paris"
        },
        {
            'question': "What is 2 + 2?",
            'choices': ["3", "4", "5", "6"],
            'correct_answer': "4"
        },
        {
            'question': "Which planet is known as the Red Planet?",
            'choices': ["Earth", "Mars", "Jupiter", "Saturn"],
            'correct_answer': "Mars"
        }
    ]

    score = 0
    for q in questions:
        if ask_question(q['question'], q['choices'], q['correct_answer']):
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
        print()

    print(f"Quiz Over! Your final score is {score}/{len(questions)}.")

if __name__ == "__main__":
    main()
