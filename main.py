from game import Hangman
from ui import UI

if __name__ == "__main__":
    ui = UI()
    game = Hangman(ui=ui, nb_guesses=10)
    game.run()
