class Square():

    def __init__(self, x, y, piece = None):

        self.x = x
        self.y = y
        self.piece = piece

    def delete_piece(self):
        self.piece = None

    def set_piece(self, piece):
        piece.set_has_moved()
        self.piece = piece

    def get_piece(self):
        
        return self.piece
    
    def get_coordinates(self):
        
        return [self.x, self.y]
    
    def has_piece(self):
        
        if not(self.piece == None):    
            return True
        else:
            return False
        
    def __str__(self):
        if self.has_piece() == True:
            piece = self.get_piece()
            colour = piece.get_colour()
            return f'The square is [{(self.x, self.y)}] and has the Piece {piece.get_letter()} which is of the colour {colour}'
        
        return f'The square is [{(self.x, self.y)}] and does not have a Piece'

