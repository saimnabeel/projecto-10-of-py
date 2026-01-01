import colorama
from colorama import Fore, Style
from colorama import Fore, Back, Style, init

# init() enables colorama functionality, especially for Windows
# autoreset=True ensures the color resets after each print statement
init(autoreset=True) 

# Example of a success message (green) and an error message (red)
print(Fore.GREEN + "Quiz complete! You scored 2 out of 4 questions correctly.")
print(Fore.YELLOW + "Your Final percentage is: 50.00%")
print(Back.RED + Fore.WHITE + Style.BRIGHT + "Wrong! The correct answer was 'd'.") # Bright white text on red background





def run_quiz():
    questions = [
        {
            "prompt": "What is the best-selling electric car of all time?\n(a) Chevrolet Bolt\n(b) Nissan Leaf\n(c) Tesla Model 3\n(d) BMW i3",
            "answer": "c"
        },
        {
            "prompt": "Which car company is known for its 'quattro' all-wheel drive system?\n(a) Mercedes-Benz\n(b) Audi\n(c) BMW\n(d) Lexus",
            "answer": "b"
        },
        {
            "prompt": "What does the 'GTI' in Volkswagen Golf GTI stand for?\n(a) Grand Touring Injection\n(b) Great Track Interface\n(c) General Transport Issue\n(d) German Turbo Innovation",
            "answer": "a"
        },
        {
            "prompt": "Which country is the manufacturer Ferrari based in?\n(a) Germany\n(b) United States\n(c) Japan\n(d) Italy",
            "answer": "d"
        }
    ]

    score = 0

    print("Welcome to the Car Quiz!")

    for question in questions:
        print("\n--------------------------")
        print(question["prompt"])
        user_answer = input("Enter your answer (a, b, c, or d): ").lower()

        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was '{question['answer']}'.")

    print("\n--------------------------")
    print(f"Quiz complete! You scored {score} out of {len(questions)} questions correctly.")
    print(f"Your final percentage is: {(score / len(questions)) * 100:.2f}%")

if __name__ == "__main__":
    run_quiz()
