from Board import *
from Player import *

class Game:
    
    def __init__(self):

        self.board = Board()
        self.white_player = Player("White")
        self.black_player = Player("Black")
        self.current_player = self.white_player
        self.game_state = True

    def allowed_moves_for_that_square(self, x, y):

        square = self.board.get_square(x,y)
        
        if square.has_piece() == True:

            piece = square.get_piece()
            colour = piece.get_colour()
            if colour != self.current_player.get_colour():
                return set()
            else:
                moves = piece.allowed_moves(x, y, self) 
                return moves
        else:
            return set()

    def make_move(self, move_from, move_to):

        move_from_x = move_from[0]
        move_from_y = move_from[1]

        move_to_x = move_to[0]
        move_to_y = move_to[1]

        square_to_move_from = self.board.get_square(move_from_x, move_from_y)
        square_to_move_to = self.board.get_square(move_to_x, move_to_y)

        piece_to_move = square_to_move_from.get_piece()

        square_to_move_to.set_piece(piece_to_move)
        square_to_move_from.delete_piece()

        if self.current_player.get_colour() == "White":
            self.current_player = self.black_player
        else:
            self.current_player = self.white_player

    def get_current_player(self):

        return self.current_player
    
    def get_board(self):
        return self.board

    def get_state(self):
        return self.game_state

    def __str__(self):
        string_from_board = self.get_board().print()
        return string_from_board


