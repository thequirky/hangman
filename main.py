import random
import os

from config import DICTIONARY_PATH, NB_GUESSES, VALID_LETTERS

# buggy_words = ["FIREPLACE", "FITTINGLY"]


def clear_screen() -> None:
    os.system("clear")


def choose_random_word() -> str:
    words = []
    with open(DICTIONARY_PATH) as f:
        for line in f:
            word = line.strip().split("'")[0].upper()
            words.append(word)
    chosen_word = random.choice(words)
    return chosen_word


def display_hidden_word(word: str, correct_guesses: str) -> None:
    revealed = ""
    for letter in word:
        if letter in correct_guesses:
            revealed += letter + " "
        else:
            revealed += "_ "
    print(revealed)


def get_letter() -> str:
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1:
            if guess in VALID_LETTERS or guess in VALID_LETTERS.lower():
                return guess.upper()
        print("Invalid guess... use letters only...")


def is_letter_in_word(letter: str, word: str) -> bool:
    return letter in word


def game(nb_guesses: int = NB_GUESSES):
    guesses_left = nb_guesses
    incorrect_guesses = []
    correct_guesses = []
    letters_found = 0
    word = choose_random_word()

    while True:
        clear_screen()
        display_hidden_word(word, correct_guesses)
        print(
            f"\n{guesses_left} guesses left. Already guessed: {', '.join(incorrect_guesses)}"
        )
        print("\n")
        guess = get_letter()
        if is_letter_in_word(guess, word):
            correct_guesses.append(guess)
            letters_found += word.count(guess)

            if letters_found == len(word):
                print(f"\nCongrats, you found the word! The word was {word}!!!\n")
                break
        else:
            if guess not in incorrect_guesses:
                incorrect_guesses.append(guess)
            guesses_left -= 1
            if guesses_left == 0:
                print(f"\nNo guesses left... Game over... The word was {word}...\n")
                break


if __name__ == "__main__":
    game()
