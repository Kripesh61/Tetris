import pygame
import random
import os
from constants import *
from game_objects import Piece

# Initialize Pygame
pygame.init()
pygame.mixer.init()

def load_sound(file):
    return pygame.mixer.Sound(file) if os.path.exists(file) else None





