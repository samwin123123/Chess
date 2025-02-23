from Square import *
from Piece import *


class Board:

    def __init__(self):
        self.squares = []

        for i in range(8):
            for j in range(8):
                
                if i == 0 or i == 1:
                    piece_color = "White"  # Changed 'type' to 'piece_color' for clarity
                
                elif i == 6 or i == 7:  # Fixed row condition for Black pieces
                    piece_color = "Black"
                else:
                    piece_color = None

                if piece_color is None:
                    self.squares.append(Square(i, j))
                else:
                    self.squares.append(Square(i, j, self.type_of_piece(j, i, piece_color)))  # Added 'self.' here


    def type_of_piece(self, j, i, piece_color):
        
        piece = None

        if i == 0 or i == 7:
            
            if j == 0 or j == 7:
                piece = Rook(piece_color)   

            elif j == 1 or j == 6: 
                piece = Horse(piece_color)

            elif j == 2 or j == 5:
                piece = Bishop(piece_color)

            elif j == 3:
                piece = Queen(piece_color)  # Queen starts on column 4 for White (left to right)

            elif j == 4:
                piece = King(piece_color)  # King starts on column 5 for White (left to right)
    
        elif i == 1 or i == 6:
            piece = Pawn(piece_color)

        return piece
    
    def get_pieces(self, colour):

        pieces = []
        for i in range(8):
            for j in range(8):
                current_square = self.get_correct_square(i, j)
                piece = current_square.get_piece()
                if piece is not None:
                    current_colour = piece.get_colour()
                    if current_colour == colour:
                        pieces.append(piece)

    
    def get_piece(self, x, y):

        current_square = self.get_square(x, y)

    def get_square(self, x, y):

        return self.squares[x*8 + y]
        
    def print(self):

        board_printed = ""
    
        for i in range(8):
            for j in range(8):
                cur_square = self.get_correct_square(i,j)
                if cur_square.has_piece() == True:
                    piece = cur_square.get_piece()
                    board_printed += piece.get_letter()
                else:
                    board_printed += "-"

                board_printed += " "
            board_printed += "\n" 
            
        return board_printed