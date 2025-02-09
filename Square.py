class Square():


    def __init__(self, x, y, piece = None):

        self.x = x
        self.y = y
        self.piece = piece

    def get_piece(self):
        
        return self.piece