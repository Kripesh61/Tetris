import pygame
import random
import os
from constants import *

class Piece: 
    def __init__(self, x, y, shape, is_bomb=False):
        self.x = x
        self.y = y
        self.shape = shape
        self.is_bomb = is_bomb
        if is_bomb: self.shape = [[1]]

def get_high_score():
            if not os.path.exists(HS_FILE): return 0
            with open(HS_FILE, "r") as f:
                try: return int(f.read())
                except: return 0

def save_high_score(self,new_score):
             if new_score > self.get_high_score():
                with open(HS_FILE, "w") as f: f.write(str(new_score))

def create_grid(locked_pos={}):
         grid = [[BLACK for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
         for (x, y), color in locked_pos.items():
              if y >= 0: grid[y][x] = color
              return grid
         
def valid_space(piece, grid):
         accepted_pos = [(j, i) for i in range(GRID_HEIGHT) for j in range(GRID_WIDTH) if grid[i][j] == BLACK]
         for y, row in enumerate(piece.shape):
             for x, val in enumerate(row):
                  if val:
                    pos = (piece.x + x, piece.y + y)
                    if pos[1] >= 0 and pos not in accepted_pos: return False
                    if pos[0] < 0 or pos[0] >= GRID_WIDTH or pos[1] >= GRID_HEIGHT: return False  
         return True 
              

