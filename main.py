from ui import UI
from game import Hangman
from config import WITH_WORD


if __name__ == "__main__":
    ui = UI()
    game = Hangman(ui=ui, with_word=WITH_WORD)
    game.run()
