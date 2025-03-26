from Game import *
from visualizing_board import *
import pygame
import sys

def main():
    game = Game()
    clock = pygame.time.Clock()
    running = True
    global WIN
    previous_press = None

    # Use a set to store selected squares. Each element is a tuple: (row, col)
    selected_squares = set()

    while running:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                WIN = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                x, y = event.pos    
                width, height = WIN.get_size()
                square_size = min(width, height) // COLS
                col = x // square_size
                row = y // square_size
                
                if (row, col) in selected_squares:
                    game.make_move(previous_press, (row, col))
                    selected_squares = ()
                else:
                    selected_squares = set()
                    # Determine which square was clicked.
                    selected_squares = game.allowed_moves_for_that_square(row,col)

                    previous_press = (row, col)

        draw_game_board(game, selected_squares)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
