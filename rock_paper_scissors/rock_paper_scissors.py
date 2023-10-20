import random

# Function to get the user's choice
def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Main game loop
user_score = 0
computer_score = 0

while True:
    print("\nRock-Paper-Scissors Game")
    
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)
    
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1
    
    print(f"\nScore - You: {user_score}  Computer: {computer_score}")
    
    play_again = input("Do you want to play another round? (yes/no): ").lower()
    if play_again not in ["yes", "y"]:
        print("Thanks for playing!")
        break
