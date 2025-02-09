class Piece:
    
    def __init__(self, colour):

        self.colour
        self.has_moved = False

class Rook(Piece):
    
    def __init__(self, colour):
        super().__init__(colour)  # Initialize x and y using the parent class constructor

class Horse(Piece):
    
    def __init__(self, colour):
        super().__init__(colour)  # Initialize x and y using the parent class constructor

class Bishop(Piece):
    
    def __init__(self, colour):
        super().__init__(colour)  # Initialize x and y using the parent class constructor

class Queen(Piece):
    
    def __init__(self, colour):
        super().__init__(colour)  # Initialize x and y using the parent class constructor


class King(Piece):
    
    def __init__(self, colour):
        super().__init__(colour)  # Initialize x and y using the parent class constructor

class Pawn(Piece):
    
    def __init__(self, colour):
        super().__init__(colour)  # Initialize x and y using the parent class constructor
