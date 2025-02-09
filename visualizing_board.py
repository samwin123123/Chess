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
    "pawn": "pictures/black_pawn.png",
    "rook": "pictures/black_rook.png",
    "knight": "pictures/black_knight.png",
    "bishop": "pictures/black_bishop.png",
    "queen": "pictures/black_queen.png",
    "king": "pictures/black_king.png"
}





def draw_board(win, width, height):
    square_size = min(width, height) // COLS  # Ensure squares remain square-shaped
    win.fill(WHITE)  # Fill background with white to avoid artifacts

    for row in range(ROWS):
        for col in range(COLS):
            rect = (col * square_size, row * square_size, square_size, square_size)
            if (row + col) % 2 == 1:
                pygame.draw.rect(win, BLACK, rect)

    # Resize and draw the piece on square (1, 0)
    piece_image = pygame.transform.scale(piece_image_original, (square_size, square_size))
    win.blit(piece_image, (1 * square_size, 0 * square_size))


def main():
    clock = pygame.time.Clock()
    running = True
    width, height = INITIAL_WIDTH, INITIAL_HEIGHT
    global WIN

    while running:
        clock.tick(60)  # Limit the frame rate to 60 FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                width, height = event.w, event.h
                WIN = pygame.display.set_mode((width, height), pygame.RESIZABLE)

        draw_board(WIN, width, height)
        pygame.display.flip()  # Update the display

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
