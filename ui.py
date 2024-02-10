from config import DICTIONARY, VALID_LETTERS

import random
import os


class UI:
    @staticmethod
    def clear_screen() -> None:
        os.system("clear")

    @staticmethod
    def choose_random_word() -> str:
        words = []
        with open(DICTIONARY) as f:
            for line in f:
                word = line.strip().split("'")[0]
                if len(word) > 3 and len(set(word)) > 1 and word.capitalize() == word:
                    words.append(word.upper())
        return random.choice(words)

    @staticmethod
    def get_letter() -> str:
        while True:
            guess = input("Guess a letter: ")
            if len(guess) == 1:
                if guess in VALID_LETTERS or guess in VALID_LETTERS.lower():
                    return guess.upper()
            print("Invalid guess... Use letters only.")

    @staticmethod
    def display_msg(msg: str) -> None:
        print(msg)

    @staticmethod
    def display_round_msg(guesses_left: int, incorrect_guesses: list[str]) -> None:
        print(
            f"\n{guesses_left} guesses left. Already guessed: {', '.join(incorrect_guesses)}\n"
        )

    @staticmethod
    def display_win_msg() -> None:
        print("\nCongrats, you found the word! You won!\n")

    @staticmethod
    def display_lost_msg(word: str) -> None:
        print(f"\nNo guesses left... Game over... The word was {word}.\n")
