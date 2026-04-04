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

def draw_window(surface, grid, score, high_score, choosing, next_p, game_over):
    surface.fill((15, 15, 30))
    f_main = pygame.font.SysFont('Arial', 30, bold=True)
    f_sub = pygame.font.SysFont('Arial', 20)
    
    # Grid Rendering
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            pygame.draw.rect(surface, grid[y][x], (GAME_X + x*BLOCK_SIZE, GAME_Y + y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
            pygame.draw.rect(surface, (40, 40, 60), (GAME_X + x*BLOCK_SIZE, GAME_Y + y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)
    
    pygame.draw.rect(surface, WHITE, (GAME_X, GAME_Y, GRID_WIDTH*BLOCK_SIZE, GRID_HEIGHT*BLOCK_SIZE), 2)

    # Sidebar Stats
    surface.blit(f_sub.render(f'High Score: {high_score}', True, (255, 215, 0)), (SIDEBAR_X, 60))
    surface.blit(f_sub.render(f'Score: {score}', True, (0, 255, 0)), (SIDEBAR_X, 90))
    surface.blit(f_sub.render('NEXT:', True, WHITE), (SIDEBAR_X, 160))

    for y, row in enumerate(next_p.shape):
        for x, val in enumerate(row):
            if val:
                if next_p.is_bomb: pygame.draw.circle(surface, next_p.color, (SIDEBAR_X + x*30+15, 200 + y*30+15), 12)
                else: pygame.draw.rect(surface, next_p.color, (SIDEBAR_X + x*30, 200 + y*30, 28, 28))

    if choosing:
        overlay = pygame.Surface((600, 650), pygame.SRCALPHA); overlay.fill((0,0,0,180))
        surface.blit(overlay, (0,0))
        surface.blit(f_sub.render("POWERUP! PRESS 1-5", True, (255, 215, 0)), (210, 300))

    if game_over:
        overlay = pygame.Surface((600, 650), pygame.SRCALPHA); overlay.fill((120,0,0,200))
        surface.blit(overlay, (0,0))
        surface.blit(f_main.render("GAME OVER", True, WHITE), (210, 280))
        surface.blit(f_sub.render("R to Restart | Q to Quit", True, WHITE), (195, 330))


def main():
    win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        locked_pos = {}
        run, choosing_mode, game_over = True, False, False
        current_p = Piece(4, 0, random.choice(SHAPES))
        next_p = Piece(4, 0, random.choice(SHAPES), random.random() < 0.25)
        clock = pygame.time.Clock()
        fall_time, score, placements = 0, 0, 0
        play_bgm()
        
         











