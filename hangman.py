import random

guessable_words = ['frog', 'space', 'hello', 'computer', 'banana', 'pizza', 'library', 'guitar', 'snowflake', 'perfume']

print("Welcome to hangman!")
print("Guess a letter: ")

def main():
    word = random.choice(guessable_words)
    answer = []
    tries_left = 5
    print(f"The word to guess has {len(word)} letters, and you have {tries_left} tries left.")
    while True:
        guess = str(input("Guess a letter: ")).lower()
        if guess in word:
            print("You guessed correctly!")
            answer.append(guess)
            print("Correct guesses so far:", answer)
        else:
            print("Not correct, try again...")
            tries_left -= 1
            print(f"You have , {tries_left} tries left.")
        if all(letter in answer for letter in word):
            print("Congratulations! You've guessed the word:", word)
            break

main()
    