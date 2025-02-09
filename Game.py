from Board import *


class Game:
    
    def __init__(self):

        self.board = Board()
        self.white_player = Player("black")
        self.black_player = Player("white")
        self.current_player = self.white_player


