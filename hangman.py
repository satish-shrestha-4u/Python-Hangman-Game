"""
Python Hangman Game

A simple command-line Hangman game built with Python.

Concepts practiced:
- random word selection
- while loops
- conditional statements
- lists and strings
- user input
- basic input validation
"""


import random


WORDS = ["hangman", "banana", "python", "tiramisu", "elephant", "laptop"]

HANGMAN_PICS = [
    "",
    " O ",
    " O\n | ",
    " O\n/| ",
    " O\n/|\\",
    " O\n/|\\\n/  ",
    " O\n/|\\\n/ \\",
]


def choose_word(words):
    """Return a random word from the word list."""
    return random.choice(words)


def update_hidden_word(secret_word, hidden_word, guessed_letter):
    """Reveal correctly guessed letters in the hidden word."""
    hidden_word_list = list(hidden_word)

    for index, letter in enumerate(secret_word):
        if letter == guessed_letter:
            hidden_word_list[index] = guessed_letter

    return "".join(hidden_word_list)


def play_hangman():
    """Run the Hangman game."""
    secret_word = choose_word(WORDS)
    hidden_word = "_" * len(secret_word)

    correct_guesses = []
    wrong_guesses = []
    mistakes = 0
    max_mistakes = 6

    print("Welcome to Hangman!")
    print("Guess the word:", " ".join(hidden_word))

    while mistakes < max_mistakes:
        user_input = input("\nGuess a letter: ").lower().strip()

        if len(user_input) != 1 or not user_input.isalpha():
            print("Please enter one letter only.")
            continue

        if user_input in correct_guesses or user_input in wrong_guesses:
            print("Already guessed. Try another letter.")
            continue

        if user_input in secret_word:
            correct_guesses.append(user_input)
            hidden_word = update_hidden_word(secret_word, hidden_word, user_input)
            print("Correct guess!")
            print("Word:", " ".join(hidden_word))
        else:
            wrong_guesses.append(user_input)
            mistakes += 1
            print("Wrong guess.")
            print(HANGMAN_PICS[mistakes])
            print("Wrong guesses:", ", ".join(wrong_guesses))
            print("Lives remaining:", max_mistakes - mistakes)
            print("Word:", " ".join(hidden_word))

        if "_" not in hidden_word:
            print("\nYou won!")
            print("The word was:", secret_word)
            break

    if mistakes == max_mistakes:
        print("\nGame over. You were hanged.")
        print("The word was:", secret_word)


if __name__ == "__main__":
    play_hangman()
