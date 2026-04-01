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
            