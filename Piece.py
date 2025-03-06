class Piece:
    
    def __init__(self, colour):

        self.colour = colour
        self.has_moved = False
        self.letter = ""
        self.moved_last_turn = False
        self.has_moved = False

    def Rock_direction(self, game, x, y, x_offseter, y_offseter):

        board = game.get_board()
        allowed_moves = set()
        
        for i in range(1, 8):

            cur_x = x + x_offseter*i
            cur_y = y + y_offseter*i

            if not(0 <= cur_x <= 7 and 0 <= cur_y <= 7):
                break

            current_square = board.get_square(cur_x, cur_y)
            
            if current_square.has_piece() != True:
                allowed_moves.add((cur_x, cur_y))
            else:
                piece = current_square.get_piece()
                colour = piece.get_colour()
                if self.colour != colour:
                    allowed_moves.add((cur_x, cur_y))
                break

        return allowed_moves

    def Bischop_direction(self, game, x, y, x_offseter, y_offseter):
    
        allowed_moves = set()
        board = game.get_board()

        # Offset upper_left
        for i in range(1,8):
            cur_x = x + x_offseter*i
            cur_y = y + y_offseter*i 
            
            if not (0 <= cur_x <= 7 and 0 <= cur_y <= 7):
                break
        
            cur_square = board.get_square(cur_x, cur_y)
            
            if cur_square.has_piece() == False:
                allowed_moves.add((cur_x, cur_y))
                continue
            
            piece = cur_square.get_piece()
            colour = piece.get_colour()
            
            if self.colour == colour:
                break

            allowed_moves.add((cur_x, cur_y))
            break

        return allowed_moves
    
    def get_letter(self):
        return self.letter
    
    def get_colour(self):
        return self.colour

    def allowed_moves(self, x, y, game):
        hej = set()
        hej.add((x, y))
        hej.add((1,1))
        return hej
    
    def set_has_moved(self):
        self.has_moved = True

class Rook(Piece):
    
    def __init__(self, colour):
        super().__init__(colour)  # Initialize x and y using the parent class constructor    
        self.letter = "R"

    def allowed_moves(self, x, y, game):

        allowed_moves = set()
        board = game.get_board()
        moves = [(1,0), (-1,0), (0,1), (0,-1)]

        for move in moves:
            allowed_moves = allowed_moves | self.Rock_direction(game, x, y, move[0], move[1])

        return allowed_moves

class Horse(Piece):
    
    def __init__(self, colour):
        super().__init__(colour)  # Initialize x and y using the parent class constructor
        self.letter = "H"

    def allowed_moves(self, x, y, game):
        
        allowed_moves = set()

        board = game.get_board()
        moves_to_check = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (-1,2), (1,-2), (-1,-2)]

        for move in moves_to_check:

            cur_x = move[0] + x
            cur_y = move[1] + y

            if 0<=cur_x and cur_x<=7 and 0<=cur_y and cur_y<=7:
                cur_square = board.get_square(cur_x, cur_y)
                if cur_square.has_piece() == False:
                    allowed_moves.add((cur_x, cur_y))
                else:
                    piece = cur_square.get_piece()
                    colour = piece.get_colour()
                    if self.colour != colour:
                        allowed_moves.add((cur_x, cur_y))
        return allowed_moves
                
class Bishop(Piece):
    
    def __init__(self, colour):
        super().__init__(colour)  # Initialize x and y using the parent class constructor
        self.letter = "B"

    def allowed_moves(self, x, y, game):
        
        allowed_moves = set()
        moves = [(1,1), (1,-1), (-1,1), (-1,-1)]
        for move in moves:
            allowed_moves = allowed_moves | self.Bischop_direction(game, x, y, move[0], move[1])
        return allowed_moves

class Queen(Piece):
    
    def __init__(self, colour):
        super().__init__(colour)  # Initialize x and y using the parent class constructor
        self.letter = "Q"

    def allowed_moves(self, x, y, game):
        
        allowed_moves = set()
        board = game.get_board()
        moves = [(1,0), (-1,0), (0,1), (0,-1)]

        for move in moves:
            allowed_moves = allowed_moves | self.Rock_direction(game, x, y, move[0], move[1])

        moves = [(1,1), (1,-1), (-1,1), (-1,-1)]
        for move in moves:
            allowed_moves = allowed_moves | self.Bischop_direction(game, x, y, move[0], move[1])

        return allowed_moves

class King(Piece):
    
    def __init__(self, colour):
        super().__init__(colour)  # Initialize x and y using the parent class constructor
        self.letter = "K"


    def allowed_moves(self, x, y, game):
        
        allowed_moves = set()

        board = game.get_board()
        moves_to_check = [(1,0), (-1,0), (0,1), (0,-1)]

        for move in moves_to_check:
            cur_x = x + move[0]
            cur_y = y + move[0]

            if 0 <= cur_x <= 7 and 0 <= cur_y <= 7:

                cur_square = board.get_square(cur_x, cur_y)

                if cur_square.has_piece() == False:
                    allowed_moves.add((cur_x, cur_y))
                    continue
                piece = cur_square.get_piece()
                colour = piece.get_colour()
                
                if self.colour != colour:
                    allowed_moves.add((cur_x, cur_y))

        return allowed_moves

class Pawn(Piece):
    
    def __init__(self, colour):
        super().__init__(colour)  # Initialize x and y using the parent class constructor
        self.letter = "P"

    def allowed_moves(self, x, y, game):

        allowed_moves = set()
        board = game.get_board()

        if self.colour == "White":
            offset = -1
        else:
            offset = 1

        for i in [1,2]:
            cur_offset = offset*i

            if i == 2 and self.has_moved == True:
                continue

            cur_x = x + cur_offset

            if 0 <= cur_x and cur_x <= 7:
                cur_square = board.get_square(cur_x, y)
                if cur_square.has_piece() == False:
                    allowed_moves.add((cur_x, y))
        

        cur_x = x + offset
        cur_y = y

        for i in [-1,1]:
            cur_y = y + i
            cur_square = board.get_square(cur_x, cur_y)
            
            if cur_square.has_piece() == False:
                continue
            piece = cur_square.get_piece()
            colour = piece.get_colour()
            
            if self.colour == colour:
                continue

            allowed_moves.add((cur_x, cur_y))
    
        return allowed_moves
        
