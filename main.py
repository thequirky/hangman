import random
import os


VALID_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DICTIONARY = "words.txt"
NB_GUESSES = 10
WITH_WORD = ""


class Hangman:
    def __init__(self) -> None:
        self.guesses_left = NB_GUESSES
        self.incorrect_guesses = []
        self.correct_guesses = []
        self.nb_letters_found = 0
        self.word = WITH_WORD.upper() or self.choose_random_word()

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

    def display_hidden_word(self) -> None:
        revealed = ""
        for letter in self.word:
            if letter in self.correct_guesses:
                revealed += letter + " "
            else:
                revealed += "_" + " "
        print(revealed)

    @staticmethod
    def get_letter() -> str:
        while True:
            guess = input("Guess a letter: ")
            if len(guess) == 1:
                if guess in VALID_LETTERS or guess in VALID_LETTERS.lower():
                    return guess.upper()
            print("Invalid guess... Use letters only.")

    def run(self) -> None:
        while True:
            self.clear_screen()
            self.display_hidden_word()
            print(
                f"\n{self.guesses_left} guesses left. Already guessed: {', '.join(self.incorrect_guesses)}\n"
            )
            guess = self.get_letter()
            if guess in self.word:
                if guess not in self.correct_guesses:
                    self.correct_guesses.append(guess)
                    self.nb_letters_found += self.word.count(guess)
                if self.nb_letters_found == len(self.word):
                    print(
                        f"\nCongrats, you found the word! The word was {self.word}.\n"
                    )
                    break
            else:
                if guess not in self.incorrect_guesses:
                    self.incorrect_guesses.append(guess)
                    self.guesses_left -= 1
                if self.guesses_left == 0:
                    print(
                        f"\nNo guesses left... Game over... The word was {self.word}.\n"
                    )
                    break


if __name__ == "__main__":
    game = Hangman()
    game.run()
