__all__ = ['main']

import pygame_menu


from random import randrange
from typing import Tuple, Any, Optional, List

from main import *
# Constants and global variables
my_file = open("scores.txt", "r")

list_of_lists = []
for line in my_file:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  list_of_lists.append(line_list)

my_file.close()

print(list_of_lists)
ABOUT = [
         'Author: Weronika Tomczuk',
         'I am student of applied mathematics at the \nWrocław University of Science and Technology.\n'
         'I made this game for Programming course.']
Instructions=['The aim in Tetris is simple. \n'
              'You bring down blocks from the top of the screen.\n '
              'You can move the blocks around,\n '
              'either left to right and/or you can rotate them.\n '
              'The blocks fall at a certain rate,\n '
              'but you can make them fall faster\n '
              'if you’re sure of your positioning.\n '
              'Your objective is to get all the blocks\n '
              'to fill all the empty space in a line at the bottom of the screen.\n '
              'Whenever you do this,\n '
              'you’ll find that the blocks vanish and you get awarded some points.\n'
              'A goal gives us a reason to play the game.\n '
              'Tetris offers an incredibly simple reason\n '
              'to play—pitting your wits against the computerized block dropper\n '
              'in order to last as long as you can.']
DIFFICULTY = ['EASY']
FPS = 60
WINDOW_SIZE = (800, 700)


#background_image = pygame_menu.BaseImage(
 #       'rainbow.png'
  #  )
#background_image.draw(win)


def change_difficulty(value: Tuple[Any, int], difficulty: str):
    """
    Change difficulty of the game.
    :param value: Tuple containing the data of the selected object
    :param difficulty: Optional parameter passed as argument to add_selector
    """
    selected, index = value
    print('Selected difficulty: "{0}" ({1}) at index {2}'
          ''.format(selected, difficulty, index))
    DIFFICULTY[0] = difficulty


def random_color():
    """
    Return a random color.
    :return: Color tuple
    """
    return randrange(0, 12), randrange(0, 178), randrange(0,31)


def play_function(difficulty: List, font: 'pygame.font.Font', test: bool = False) -> None:
    """
    Main game function.
    :param difficulty: Difficulty of the game
    :param font: Pygame font
    :param test: Test method, if ``True`` only one loop is allowed
    :return: None
    """
    assert isinstance(difficulty, list)
    difficulty = difficulty[0]
    assert isinstance(difficulty, str)

    # Define globals
    global main_menu
    global clock

    if difficulty == 'EASY':
        f = font.render('Playing as a baby (easy)', True, (255, 255, 255))
    elif difficulty == 'MEDIUM':
        f = font.render('Playing as a kid (medium)', True, (255, 255, 255))
    elif difficulty == 'HARD':
        f = font.render('Playing as a champion (hard)', True, (255, 255, 255))
    else:
        raise ValueError('unknown difficulty {0}'.format(difficulty))
    f_esc = font.render('Press ESC to open the menu', True, (255, 255, 255))

    # Draw random color and text
    bg_color = random_color()

    # Reset main menu and disable
    # You also can set another menu, like a 'pause menu', or just use the same
    # main_menu as the menu that will check all your input.
    main_menu.disable()
    main_menu.full_reset()

    frame = 0

    while True:

        # noinspection PyUnresolvedReferences
        clock.tick(60)
        frame += 1

        # Application events
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    main_menu.enable()

                    # Quit this function, then skip to loop of main-menu on line 256
                    return

        # Pass events to main_menu
        if main_menu.is_enabled():
            main_menu.update(events)

        # Continue playing
        surface.fill(bg_color)
        surface.blit(f, (int((WINDOW_SIZE[0] - f.get_width()) / 2),
                         int(WINDOW_SIZE[1] / 2 - f.get_height())))
        surface.blit(f_esc, (int((WINDOW_SIZE[0] - f_esc.get_width()) / 2),
                             int(WINDOW_SIZE[1] / 2 + f_esc.get_height())))
        pygame.display.flip()

        # If test returns
        if test and frame == 2:
            break
        main(win)

def main_background():
    """
    Function used by menus, draw on background while menu is active.
    :return: None
    """
    global surface
    surface.fill((0, 0, 0))
    #surface = pygame.Surface((800, 700))
    #surface = surface.convert_alpha()
    #surface.fill((0, 0, 0, 0))
    #image = pygame.Surface([640, 480], pygame.SRCALPHA)
    #background_image = pygame_menu.BaseImage(
    #    'rainbow.png'
    #)
    #background_image.draw(win)


def menu(test: bool = False):
    """
    Main program.
    :param test: Indicate function is being tested
    :return: None
    """


    # Globals

    global clock
    global main_menu
    global surface


    # Create window

    surface = pygame.display.set_mode(WINDOW_SIZE)
    clock = pygame.time.Clock()


    # Create menus: Play Menu

    play_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.7,
        title='Play Menu',
        width=WINDOW_SIZE[0] * 0.75
    )

    submenu_theme = pygame_menu.themes.THEME_DEFAULT.copy()
    submenu_theme.widget_font_size = 15
    play_submenu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.5,
        theme=submenu_theme,
        title='Submenu',
        width=WINDOW_SIZE[0] * 0.7
    )
    for i in range(30):
        play_submenu.add.button('Back {0}'.format(i), pygame_menu.events.BACK)
    play_submenu.add.button('Return to main menu', pygame_menu.events.RESET)

    play_menu.add.button('Start',  # When pressing return -> play(DIFFICULTY[0], font)
                         play_function,
                         DIFFICULTY,
                         pygame.font.Font(pygame_menu.font.FONT_FRANCHISE, 30))
    play_menu.add.selector('Select difficulty ',
                           [('1 - Easy', 'EASY'),
                            ('2 - Medium', 'MEDIUM'),
                            ('3 - Hard', 'HARD')],
                           onchange=change_difficulty,
                           selector_id='select_difficulty')

    play_menu.add.button('Return to main menu', pygame_menu.events.BACK)

    #highscores
    scores_theme = pygame_menu.themes.THEME_DEFAULT.copy()
    scores_theme.widget_margin = (0, 0)

    scores_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.6,
        theme=scores_theme,
        title='Highscores',
        width=WINDOW_SIZE[0] * 0.6
    )
    list=['1. The best','2. The second best','3. The third best']
    zip_iterator = zip(list, list_of_lists)
    dic = dict(zip_iterator)
    for key in dic:

        scores_menu.add.label('       {} score is {} points.'.format(key,dic[key][0]), align=pygame_menu.locals.ALIGN_LEFT, font_size=20)
    scores_menu.add.vertical_margin(30)
    scores_menu.add.button('Return to menu', pygame_menu.events.BACK)

    # Create menus:About

    about_theme = pygame_menu.themes.THEME_DEFAULT.copy()
    about_theme.widget_margin = (0, 0)

    about_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.6,
        theme=about_theme,
        title='About an author',
        width=WINDOW_SIZE[0] * 0.6
    )

    for m in ABOUT:
        about_menu.add.label(m, align=pygame_menu.locals.ALIGN_LEFT, font_size=20)
    about_menu.add.vertical_margin(30)
    about_menu.add.button('Return to menu', pygame_menu.events.BACK)

    #create instructions menu
    instruction_theme = pygame_menu.themes.THEME_DEFAULT.copy()
    instruction_theme.widget_margin = (0, 0)

    instruction_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.9,
        theme=instruction_theme,
        title='Game rules',
        width=WINDOW_SIZE[0] * 0.9
    )

    for i in Instructions:
        instruction_menu.add.label(i, align=pygame_menu.locals.ALIGN_LEFT, font_size=20)
    instruction_menu.add.vertical_margin(30)
    instruction_menu.add.button('Return to menu', pygame_menu.events.BACK)

    # -------------------------------------------------------------------------
    # Create menus: Main
    # -------------------------------------------------------------------------
    main_theme = pygame_menu.themes.THEME_DEFAULT.copy()

    main_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.6,
        theme=main_theme,
        title='Main Menu',
        width=WINDOW_SIZE[0] * 0.6
    )

    main_menu.add.button('Play', play_menu)
    main_menu.add.button('Instructions', instruction_menu)
    main_menu.add.button('Highscores', scores_menu)
    main_menu.add.button('About an author', about_menu)
    main_menu.add.button('Quit', pygame_menu.events.EXIT)


  
    # Main loop
 
    while True:

        # Tick
        clock.tick(FPS)

        # Paint background
        main_background()

        # Application events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        # Main menu
        if main_menu.is_enabled():
            main_menu.mainloop(surface, main_background, disable_loop=test, fps_limit=FPS)

        # Flip surface
        pygame.display.flip()

        # At first loop returns
        if test:
            break


if __name__ == '__main__':
    menu()
