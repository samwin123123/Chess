from Board import *
from Player import *

class Game:
    
    def __init__(self):

        self.board = Board()
        self.white_player = Player("Black")
        self.black_player = Player("White")
        self.current_player = self.white_player
        self.game_state = True

    def get_current_player(self):

        return self.current_player
    
    def get_board(self):
        return self.board

    def get_state(self):
        return self.game_state

    def __str__(self):
        string_from_board = self.get_board().print()
        return string_from_board


