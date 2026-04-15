import pygame
import random
import os
from constants import *
from game_objects import  Piece, get_high_score, save_high_score, create_grid, valid_space

# Initialize Pygame
pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()

def load_sound(file):
    if os.path.exists(file):
        return pygame.mixer.Sound(file)
    return None

# Load Assets
sfx_place = load_sound("place.wav")
sfx_explode = load_sound("explode.wav")
sfx_gameover = load_sound("gameover.wav")

def play_bgm():
    def play_bgm():
     path = os.path.join(os.path.dirname(__file__), "bgm.mp3")
    if os.path.exists(path):
        try:
            pygame.mixer.music.load(path)
            pygame.mixer.music.set_volume(0.4)
            pygame.mixer.music.play(-1)
        except Exception as e:
            print(f"⚠️ Music error: {e}")

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
        play_bgm()
        locked_pos = {}
        run, choosing_mode, game_over = True, False, False
        current_p = Piece(4, 0, random.choice(SHAPES))
        next_p = Piece(4, 0, random.choice(SHAPES), random.random() < 0.25)
        clock = pygame.time.Clock()
        fall_time, score, placements = 0, 0, 0
        play_bgm()

        while run:
            grid = create_grid(locked_pos)
            fall_time += clock.get_rawtime()
            clock.tick()
            fall_speed = max(80, 450 - ((score // 200) * 60))

            if fall_time > fall_speed and not choosing_mode and not game_over:
                fall_time = 0
                current_p.y += 1
                if not valid_space(current_p, grid):
                    current_p.y -= 1
                    if current_p.is_bomb:
                        u_pos = (current_p.x, current_p.y + 1)
                        if u_pos in locked_pos and locked_pos[u_pos] == current_p.color:
                            if sfx_explode: sfx_explode.play()
                            for i in range(current_p.x-1, current_p.x+2):
                                for j in range(current_p.y-1, current_p.y+2):
                                    if (i,j) in locked_pos: del locked_pos[(i,j)]
                            score += 50
                        elif u_pos in locked_pos: game_over = True
                    
                    if not game_over:
                        if sfx_place: sfx_place.play()
                        for y, row in enumerate(current_p.shape):
                            for x, val in enumerate(row):
                                if val: locked_pos[(current_p.x + x, current_p.y + y)] = current_p.color
                        score += 10; placements += 1
                        current_p = next_p
                        next_p = Piece(4, 0, random.choice(SHAPES), random.random() < 0.25)
                        if placements % 10 == 0: choosing_mode = True
                        if not valid_space(current_p, grid): game_over = True
            
            if game_over: pygame.mixer.music.stop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT: pygame.quit(); return
                if event.type == pygame.KEYDOWN:
                    if game_over:
                        if event.key == pygame.K_r: save_high_score(score); run = False
                        if event.key == pygame.K_q: pygame.quit(); return
                    elif choosing_mode:
                        if event.key in range(pygame.K_1, pygame.K_6):
                            current_p = Piece(4, 0, SHAPES[event.key - 49])
                            choosing_mode = False
                    else:
                        if event.key == pygame.K_LEFT:
                            current_p.x -= 1
                            if not valid_space(current_p, grid): current_p.x += 1
                        if event.key == pygame.K_RIGHT:
                            current_p.x += 1
                            if not valid_space(current_p, grid): current_p.x -= 1
                        if event.key == pygame.K_DOWN:
                            current_p.y += 1
                            if not valid_space(current_p, grid): current_p.y -= 1

            draw_window(win, grid, score, get_high_score(), choosing_mode, next_p, game_over)
            if not choosing_mode and not game_over:
                for y, row in enumerate(current_p.shape):
                    for x, val in enumerate(row):
                        if val:
                            pos = (GAME_X + (current_p.x+x)*30, GAME_Y + (current_p.y+y)*30)
                            if current_p.is_bomb: pygame.draw.circle(win, current_p.color, (pos[0]+15, pos[1]+15), 12)
                            else: pygame.draw.rect(win, current_p.color, (pos[0], pos[1], 29, 29))
            pygame.display.update()


if __name__ == "__main__":
    main()










