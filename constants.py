import pygame

# Screen & Grid

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 650
BLOCK_SIZE = 30
GRID_WIDTH, GRID_HEIGHT = 10, 18
GAME_X, GAME_Y, SIDEBAR_X = 50, 50, 400
HS_FILE = "highscore.txt"

# Colors

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = [ (0, 255, 255), (255, 255, 0), (128, 0, 128), (0, 0, 225), (255, 0, 0), (255, 165, 0), (0, 225, 0)   ]

# Custom Shapes: I, O, T, V, X

SHAPES = [ 

    [[1, 1, 1, 1]], 
    [[1, 1], [1, 1]], 
    [[0, 1, 0], [1, 1, 1]], 
    [[1, 0, 1], [0, 1, 0]], 
    [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
      
      ]

