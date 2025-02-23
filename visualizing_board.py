import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
INITIAL_WIDTH, INITIAL_HEIGHT = 640, 640  # Initial window size
ROWS, COLS = 8, 8  # Chess board dimensions

# Colors
WHITE = (232, 235, 239)
BLACK = (125, 135, 150)

# Set up the display
WIN = pygame.display.set_mode((INITIAL_WIDTH, INITIAL_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('Resizable Chess Board')

# Load piece image
# Ensure you have a piece image named 'white_horse.png' in the 'pictures' directory
piece_image_original = pygame.image.load('pictures/black_pawn.png')

piece_images_black = {
    "P": "pictures/black_pawn.png",
    "R": "pictures/black_rook.png",
    "H": "pictures/black_horse.png",
    "B": "pictures/black_bishop.png",
    "Q": "pictures/black_queen.png",
    "K": "pictures/black_king.png"
}

piece_images_white = {
    "P": "pictures/white_pawn.png",
    "R": "pictures/white_rook.png",
    "H": "pictures/white_horse.png",
    "B": "pictures/white_bishop.png",
    "Q": "pictures/white_queen.png",
    "K": "pictures/white_king.png"
}


def draw_game_board(game, selected_squares=None):
    global WIN, ROWS, COLS, WHITE, BLACK
    if selected_squares is None:
        selected_squares = set()
        
    # Retrieve the current window size
    width, height = WIN.get_size()
    square_size = min(width, height) // COLS  # ensures squares remain square

    for row in range(ROWS):
        for col in range(COLS):
            # If this square is selected, use the uniform yellow color.
            if (row, col) in selected_squares:
                board_color = (255, 255, 128)  # uniform yellow tone
            else:
                board_color = WHITE if (row + col) % 2 == 0 else BLACK

            square_rect = (col * square_size, row * square_size, square_size, square_size)
            pygame.draw.rect(WIN, board_color, square_rect)

            # Draw the piece if there is one on the square.
            board = game.get_board()
            square = board.get_square(row, col)
            if square.has_piece():
                piece = square.get_piece()
                colour = piece.get_colour()
                piece_type = piece.get_letter()  # using piece_type instead of 'type'
                
                # Look up the file path from the dictionaries
                if colour == "Black":
                    image_path = piece_images_black[piece_type]
                elif colour == "White":
                    image_path = piece_images_white[piece_type]
                else:
                    image_path = None

                if image_path is not None:
                    # Load and scale the image to fit the square
                    image = pygame.image.load(image_path)
                    piece_image_scaled = pygame.transform.scale(image, (square_size, square_size))
                    WIN.blit(piece_image_scaled, (col * square_size, row * square_size))
