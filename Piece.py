class Piece:
    
    def __init__(self, colour):

        self.colour = colour
        self.has_moved = False
        self.letter = ""

    def get_letter(self):
        return self.letter
    
    def get_colour(self):
        return self.colour

    def allowed_moves(self, x, y):
        hej = set()
        hej.add((x, y))
        hej.add((1,1))
        return hej

class Rook(Piece):
    
    def __init__(self, colour):
        super().__init__(colour)  # Initialize x and y using the parent class constructor    
        self.letter = "R"

class Horse(Piece):
    
    def __init__(self, colour):
        super().__init__(colour)  # Initialize x and y using the parent class constructor
        self.letter = "H"

class Bishop(Piece):
    
    def __init__(self, colour):
        super().__init__(colour)  # Initialize x and y using the parent class constructor
        self.letter = "B"

class Queen(Piece):
    
    def __init__(self, colour):
        super().__init__(colour)  # Initialize x and y using the parent class constructor
        self.letter = "Q"

class King(Piece):
    
    def __init__(self, colour):
        super().__init__(colour)  # Initialize x and y using the parent class constructor
        self.letter = "K"


class Pawn(Piece):
    
    def __init__(self, colour):
        super().__init__(colour)  # Initialize x and y using the parent class constructor
        self.letter = "P"