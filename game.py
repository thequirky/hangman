import random

from ui import UI

DICTIONARY = "words.txt"


class Hangman:
    def __init__(self, ui: UI, nb_guesses: int, with_word: str = "") -> None:
        self.ui = ui
        self.guesses_left = nb_guesses
        self.incorrect_guesses = []
        self.correct_guesses = []
        self.secret_word = with_word.upper() or self.choose_random_word()

    @staticmethod
    def choose_random_word() -> str:
        words = []
        with open(DICTIONARY) as f:
            for line in f:
                word = line.strip().upper()
                if len(word) > 3:
                    words.append(word)
        return random.choice(words)

    @property
    def nb_letters_found(self) -> int:
        return sum(self.secret_word.count(letter) for letter in self.correct_guesses)

    @property
    def revealed_word(self) -> str:
        revealed = ""
        for letter in self.secret_word:
            if letter in self.correct_guesses:
                revealed += letter + " "
            else:
                revealed += "_" + " "
        return revealed

    @property
    def found_all_letters(self) -> bool:
        return self.nb_letters_found == len(self.secret_word)

    def run(self) -> None:
        while True:
            self.ui.clear_screen()
            self.ui.display_msg(self.revealed_word)
            self.ui.display_round_msg(self.guesses_left, self.incorrect_guesses)
            guess = self.ui.get_letter()
            if guess in self.secret_word:
                if guess not in self.correct_guesses:
                    self.correct_guesses.append(guess)
                if self.found_all_letters:
                    self.ui.display_win_msg()
                    return
            else:
                if guess not in self.incorrect_guesses:
                    self.incorrect_guesses.append(guess)
                    self.guesses_left -= 1
                if self.guesses_left == 0:
                    self.ui.display_lost_msg(self.secret_word)
                    return
