from ui import UI
from game import Hangman


if __name__ == "__main__":
    ui = UI()
    game = Hangman(ui=ui, nb_guesses=10)

    game.run()
