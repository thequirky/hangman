import random
import os

DICTIONARY = "words.txt"
VALID_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NB_GUESSES = 10


def get_letter() -> str:
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1:
            if guess in VALID_LETTERS.upper() or guess in VALID_LETTERS.lower():
                return guess.upper()
        print("Invalid guess... Use letters only.")


def clear_screen() -> None:
    os.system("clear")


def display_round_msg(guesses_left: int, incorrect_guesses: list[str]) -> None:
    print(
        f"\n{guesses_left} guesses left. Already guessed: {', '.join(incorrect_guesses)}\n"
    )


def display_win_msg() -> None:
    print("\nCongrats, you found the word! You won!\n")


def display_lost_msg(word: str) -> None:
    print(f"\nNo guesses left... Game over... The word was {word}.\n")


def choose_random_word() -> str:
    words = []
    with open(DICTIONARY) as f:
        for line in f:
            word = line.strip().split("'")[0]
            if len(word) > 3 and len(set(word)) > 1 and word.capitalize() == word:
                words.append(word.upper())
    return random.choice(words)


def get_nb_letters_found(secret_word: str, correct_guesses: list[str]) -> int:
    return sum(secret_word.count(letter) for letter in correct_guesses)


def reveal_word(secret_word: str, correct_guesses: list[str]) -> str:
    revealed = ""
    for letter in secret_word:
        if letter in correct_guesses:
            revealed += letter + " "
        else:
            revealed += "_" + " "
    return revealed


def run() -> None:

    secret_word = choose_random_word()
    guesses_left = NB_GUESSES
    correct_guesses = []
    incorrect_guesses = []

    while True:
        clear_screen()

        reveal_word(secret_word, correct_guesses)
        display_round_msg(guesses_left, incorrect_guesses)
        guess = get_letter()
        if guess in secret_word:
            if guess not in correct_guesses:
                correct_guesses.append(guess)
            all_letters_found = get_nb_letters_found(secret_word, correct_guesses) == len(secret_word)
            if all_letters_found:
                display_win_msg()
                return
        else:
            if guess not in incorrect_guesses:
                incorrect_guesses.append(guess)
                guesses_left -= 1
            if guesses_left == 0:
                display_lost_msg(secret_word)
                return


if __name__ == "__main__":
    run()
