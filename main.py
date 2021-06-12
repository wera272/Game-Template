from window import *
def main(win):

    locked_positions = {}
    
    run = True

    clock = pygame.time.Clock()
    fall_time = 0

    level_time = 0
    score = 0

    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        clock.tick()

        if level_time/1000 > 5:
            level_time = 0
            if level_time > 0.12:
                level_time -= 0.005







        draw_window(win, grid, score)

        pygame.display.update()


