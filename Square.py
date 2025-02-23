class Square():

    def __init__(self, x, y, piece = None):

        self.x = x
        self.y = y
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