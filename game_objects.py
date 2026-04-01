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

        def save_high_score(new_score):
            if new_score > get_high_score():
                with open(HS_FILE, "w") as f: f.write(str(new_score))
                
