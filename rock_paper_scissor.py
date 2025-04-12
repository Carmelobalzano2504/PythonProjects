import random

choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0
print("Welcome to Rock, Paper, Scissors!")

while True:
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in choices:
        user_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()

    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result = "You win!"
        player_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    print(f"You chose {user_choice}, computer chose {computer_choice}. {result}")
    print(f"Your score: {player_score}, Computer's score: {computer_score}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    while play_again not in ["yes", "no"]:
        play_again = input("Invalid input. Please enter yes or no: ").lower()

    if play_again == "no":
        break



