import random
import time
from colorama import init, Fore, Style

# Initialize colorama for colored output
init(autoreset=True)

# Function to print text with a delay effect
def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Function to simulate the Magic 8-Ball response
def magic_8_ball():
    # User's name and question
    name = input("What's your name? ")
    while True:
        question = input("What question would you like to ask the Magic 8-Ball? ")
        if question.strip():  # Check if the input is not empty or whitespace
            break  # Exit the loop if the input is valid
        else:
            print("Please enter a valid question.")

    # Simulate the Magic 8-Ball "thinking"
    slow_print("Let me think about that...")
    time.sleep(1)  # Delay for 2 seconds

    # Randomly select a response from the Magic 8-Ball
    responses = [
        "Yes - definitely",
        "It is decidedly so",
        "Without a doubt",
        "Reply hazy, try again",
        "Ask again later",
        "Better not tell you now",
        "My sources say no",
        "Outlook not so good",
        "Very doubtful"
    ]
    answer = random.choice(responses)

    # Print the conversation with formatted output
    print("\n" + Fore.GREEN + "Magic 8-Ball's answer:" + Style.RESET_ALL)
    print(Fore.YELLOW + answer + Style.RESET_ALL)


# Simulate the Magic 8-Ball interaction
magic_8_ball()
