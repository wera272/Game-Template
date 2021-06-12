import pygame
from blocks import *


def create_grid(locked_pos={}):  # *
    grid = [[(0,0,0) for _ in range(10)] for _ in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_pos:
                c = locked_pos[(j,i)]
                grid[i][j] = c
    return grid

def draw_window(surface, grid, score=0, last_score = 0):
    surface.fill((128,128,128))

    pygame.font.init()
    font = pygame.font.SysFont('Berlin Sans FB', 60, bold=True)
    label = font.render('Tetris', 1, (255,255,255))

    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), 30))

    # current score
    font = pygame.font.SysFont('Berlin Sans FB', 30)
    label = font.render('Score: ' + str(score), 1, (255,255,255))

    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 - 100

    surface.blit(label, (sx + 20, sy + 160))
    # last score
    label = font.render('High Score: ' + last_score, 1, (255,255,255))

    sx = top_left_x - 200
    sy = top_left_y + 200

    surface.blit(label, (sx , sy + 160))
    font = pygame.font.SysFont('Berlin Sans FB', 30)

    label = font.render('Lives: ' + str(lives), 1, (255, 255, 255))

    sx = top_left_x -200
    sy = top_left_y +200

    surface.blit(label, (sx + 20, sy - 30))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j*block_size, top_left_y + i*block_size, block_size, block_size), 0)

    pygame.draw.rect(surface, (128, 128, 128), (top_left_x, top_left_y, play_width, play_height), 5)

    draw_grid(surface, grid)
    #pygame.display.update()
