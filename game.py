from ui import UI
from config import NB_GUESSES


class Hangman:
    def __init__(self, ui: UI, with_word: str = "") -> None:
        self.ui = ui
        self.guesses_left = NB_GUESSES
        self.incorrect_guesses = []
        self.correct_guesses = []
        self.word = with_word.upper() or self.ui.choose_random_word()

    @property
    def nb_letters_found(self) -> int:
        return sum(self.word.count(letter) for letter in self.correct_guesses)

    @property
    def revealed_word(self) -> str:
        revealed = ""
        for letter in self.word:
            if letter in self.correct_guesses:
                revealed += letter + " "
            else:
                revealed += "_" + " "
        return revealed

    @property
    def found_all_letters(self) -> bool:
        return self.nb_letters_found == len(self.word)

    def run(self) -> None:
        while True:
            self.ui.clear_screen()
            print(self.revealed_word)
            print(
                f"\n{self.guesses_left} guesses left. Already guessed: {', '.join(self.incorrect_guesses)}\n"
            )
            guess = self.ui.get_letter()
            if guess in self.word:
                if guess not in self.correct_guesses:
                    self.correct_guesses.append(guess)
                if self.found_all_letters:
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
