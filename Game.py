from Board import *
from Player import *
from copy import deepcopy

class Game:
    
    def __init__(self):

        self.board = Board()
        self.white_player = Player("White")
        self.black_player = Player("Black")
        self.current_player = self.white_player
        self.not_current_player = self.black_player
        self.game_state = True

    def change_player(self):

        if self.current_player.get_colour() == "White":
            self.current_player = self.black_player
            self.not_current_player = self.white_player
        else:
            self.current_player = self.white_player
            self.not_current_player = self.black_player

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

        self.change_player()

    def check_game_over(self):

        allowed_moves_without_chess = set()
        for cur_x in range(8):
            for cur_y in range(8):
                cur_square = self.board.get_square(cur_x, cur_y)
                cur_pos = (cur_x, cur_y)
                if cur_square.has_piece() == True:
                    piece = cur_square.get_piece()
                    colour = piece.get_colour()
                    if colour != self.current_player.get_colour():
                        continue
                    possibly_allowed = piece.allowed_moves()
                    
                    for move in possibly_allowed:
                        self.check_chess(cur_pos, move, self.not_current_player, self.current_player)

    def check_chess(self, cur_pos, move_to, attacking_player, defending_player):
        
        alternative_game = deepcopy(self)
        alternative_game.make_move(cur_pos, move_to)

        alternative_game.change_player()
        king_pos = None
        allowed_moves = set()

        for cur_x in range(8):
            for cur_y in range(8):
                cur_square = alternative_game.get_square(cur_x, cur_y)
                if cur_square.has_piece() != True:
                    continue
                piece = cur_square.get_piece()
                colour = piece.get_colour()
                if alternative_game.get_current_player.get_colour() == colour:
                    continue
                if piece.get_letter() == "K":
                    king_pos = (cur_x, cur_y)
                    break

        for cur_x in range(8):
            for cur_y in range(8):
                cur_square = alternative_game.board.get_square(cur_x, cur_y)
                cur_pos = (cur_x, cur_y)
                if cur_square.has_piece() == True:
                    piece = cur_square.get_piece()
                    colour = piece.get_colour()
                    if colour != alternative_game.current_player.get_colour():
                        continue
                    possibly_allowed = piece.allowed_moves()
                    if king_pos in possibly_allowed:
                        possibly_allowed = set()

        return

    def get_current_player(self):

        return self.current_player
    
    def get_board(self):
        return self.board

    def get_state(self):
        return self.game_state

    def __str__(self):
        string_from_board = self.get_board().print()
        return string_from_board


