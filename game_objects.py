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