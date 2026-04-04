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

# Load Assets
sfx_place = load_sound("place.wav")
sfx_explode = load_sound("explode.wav")
sfx_gameover = load_sound("gameover.wav")

def play_bgm():
    if os.path.exists("bgm.mp3"):
        pygame.mixer.music.load("bgm.mp3")
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)










