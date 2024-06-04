import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (stone, paper, or scissors): ").lower()
        if user_choice in ['stone', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please enter stone, paper, or scissors.")

def get_computer_choice():
    return random.choice(['stone', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'stone' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'stone') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Let's play Stone, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)
    print(determine_winner(user_choice, computer_choice))

# Run the game
play_game()
import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (stone, paper, or scissors): ").lower()
        if user_choice in ['stone', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please enter stone, paper, or scissors.")

def get_computer_choice():
    return random.choice(['stone', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'stone' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'stone') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Let's play Stone, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)
    print(determine_winner(user_choice, computer_choice))

# Run the game
play_game()
