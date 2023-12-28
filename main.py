import random
import os

from config import DICTIONARY, NB_GUESSES, VALID_LETTERS


def clear_screen() -> None:
    os.system("clear")


def choose_random_word() -> str:
    words = []
    with open(DICTIONARY) as f:
        for line in f:
            word = line.strip().split("'")[0].upper()
            if len(word) > 3 and len(set(word)) > 1:
                words.append(word)
    return random.choice(words)


def display_hidden_word(word: str, correct_guesses: str) -> None:
    revealed = ""
    for letter in word:
        if letter in correct_guesses:
            revealed += letter + " "
        else:
            revealed += "_" + " "
    print(revealed)


def get_letter() -> str:
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1:
            if guess in VALID_LETTERS or guess in VALID_LETTERS.lower():
                return guess.upper()
        print("Invalid guess... Use letters only.")


def hangman(nb_guesses: int = NB_GUESSES, with_word: str = ""):
    guesses_left = nb_guesses
    incorrect_guesses = []
    correct_guesses = []
    nb_letters_found = 0
    word = with_word.upper() or choose_random_word()

    while True:
        clear_screen()
        display_hidden_word(word, correct_guesses)
        print(
            f"\n{guesses_left} guesses left. Already guessed: {', '.join(incorrect_guesses)}\n"
        )
        guess = get_letter()
        if guess in word:
            if guess not in correct_guesses:
                correct_guesses.append(guess)
                nb_letters_found += word.count(guess)
            if nb_letters_found == len(word):
                print(f"\nCongrats, you found the word! The word was {word}.\n")
                break
        else:
            if guess not in incorrect_guesses:
                incorrect_guesses.append(guess)
                guesses_left -= 1
            if guesses_left == 0:
                print(f"\nNo guesses left... Game over... The word was {word}.\n")
                break


if __name__ == "__main__":
    # hangman(with_word="fireplace")
    hangman()
