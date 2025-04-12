import random


def main():
    correct_number = random.randint(1, 10)
    print('Welcome to my guessing game! \n')
    while True:
        user_input = input("Guess a number between 1 and 10: ")
        try:
            user_guess = int(user_input)
            if check_guess(user_guess, correct_number):
                break
        except ValueError:
            print("Please enter a valid number.")
            continue

def check_guess(user_guess, correct_number): 
    if user_guess == correct_number:        
        print("Congratulations! You guessed the correct number.")
        return True
    else:
        print("Sorry, that is not correct. Guess again.")
        return False
    
main()