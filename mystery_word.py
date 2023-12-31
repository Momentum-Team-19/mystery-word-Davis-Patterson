import random
import time
import json
from anipage import start_screen
from anipage1 import start_screen1
import pyfiglet
import colorama
from colorama import Fore, Back, Style
import pygame
import os
from pygame import mixer

# Line 679 print(launch_code)

colorama.init(autoreset=True)

pygame.mixer.init()

current_directory = os.path.dirname(__file__)
menu_music_path = os.path.join(
    current_directory, 'sfx', '8bittownthemesong-59266.mp3')
game_music_path = os.path.join(current_directory, 'sfx', 'martian-131602.mp3')
victory_music_path = os.path.join(
    current_directory, 'sfx', 'very-lush-and-swag-loop-74140.mp3')
gameover_music_path = os.path.join(
    current_directory, 'sfx', 'game-over-38511.mp3')
countdown_music_path = os.path.join(
    current_directory, 'sfx', 'countdown-sound-effect-8-bit-151797.mp3')

# pygame.mixer.music.load(menu_music_path)
# menu_music = pygame.mixer.Sound(menu_music_path)
# game_music = pygame.mixer.Sound(game_music_path)

very_easy_pics = {
    0: "           ___\n     |     | |\n    / \    | |\n   |--o|===|-|\n   |---|   | |\n  /     \  | |\n | U     | |-|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    1: "           ___\n           | |\n    / \    | |\n   |--o|===|-|\n   |---|   | |\n  /     \  | |\n | U     | |-|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    2: "           ___\n           | |\n      \    | |\n   |--o|===|-|\n   |---|   | |\n  /     \  | |\n | U     | |-|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    3: "           ___\n           | |\n           | |\n    --o|===|-|\n   |---|   | |\n  /     \  | |\n | U     | |-|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    4: "           ___\n           | |\n           | |\n      o|===|-|\n   |---|   | |\n  /     \  | |\n | U     | |-|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    5: "           ___\n           | |\n           | |\n        ===|-|\n   |---|   | |\n  /     \  | |\n | U     | |-|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    6: "           ___\n           | |\n           | |\n        ===|-|\n    ---|   | |\n  /     \  | |\n | U     | |-|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    7: "           ___\n           | |\n           | |\n        ===|-|\n      -|   | |\n  /     \  | |\n | U     | |-|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    8: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /     \  | |\n | U     | |-|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    9: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /        | |\n | U     | |-|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    10: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /        | |\n | U       |-|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    11: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /        | |\n | U       |-|\n |       |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    12: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /        | |\n | U       |-|\n |       |=| |\n         | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    13: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /        | |\n | U       |-|\n |       |=| |\n         | | |\n |___  __  |_|\n  |@| |@|  | |\n___________|_|_",

    14: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /        | |\n | U       |-|\n |       |=| |\n         | | |\n |___  __  |_|\n  |@|      | |\n___________|_|_",

    15: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /        | |\n | U       |-|\n |       |=| |\n         | | |\n |___  __  |_|\n           | |\n___________|_|_",
}

easy_pics = {
    0: "           ___\n     |     | |\n    / \    | |\n   |--o|===|-|\n   |---|   | |\n  /     \  | |\n | U     | |-|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    1: "           ___\n           | |\n    / \    | |\n   |--o|===|-|\n   |---|   | |\n  /     \  | |\n | U     | |-|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    2: "           ___\n           | |\n           | |\n      o|===|-|\n   |---|   | |\n  /     \  | |\n | U     | |-|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    3: "           ___\n           | |\n           | |\n        ===|-|\n    ---|   | |\n  /     \  | |\n | U     | |-|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    4: "           ___\n           | |\n           | |\n        ===|-|\n      -|   | |\n  /     \  | |\n | U     | |-|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    5: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /     \  | |\n | U     | |-|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    6: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /        | |\n | U     | |-|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    7: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /        | |\n | U       |-|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    8: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /        | |\n | U       |-|\n |       |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    9: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /        | |\n | U       |-|\n |       |=| |\n         | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    10: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /        | |\n | U       |-|\n |       |=| |\n         | | |\n |___  __  |_|\n  |@| |@|  | |\n___________|_|_",

    11: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /        | |\n | U       |-|\n |       |=| |\n         | | |\n |___  __  |_|\n  |@|      | |\n___________|_|_",

    12: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /        | |\n | U       |-|\n |       |=| |\n         | | |\n |___  __  |_|\n           | |\n___________|_|_",
}

medium_pics = {
    0: "           ___\n     |     | |\n    / \    | |\n   |--o|===|-|\n   |---|   | |\n  /     \  | |\n | U     | |-|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    1: "           ___\n           | |\n           | |\n      o|===|-|\n   |---|   | |\n  /     \  | |\n | U     | |-|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    2: "           ___\n           | |\n           | |\n        ===|-|\n    ---|   | |\n  /     \  | |\n | U     | |-|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    3: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /     \  | |\n | U     | |-|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    4: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /        | |\n | U     | |-|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    5: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /        | |\n | U       |-|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    6: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /        | |\n | U       |-|\n |       |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    7: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /        | |\n | U       |-|\n |       |=| |\n         | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    8: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /        | |\n | U       |-|\n |       |=| |\n         | | |\n |___  __  |_|\n  |@| |@|  | |\n___________|_|_",

    9: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /        | |\n | U       |-|\n |       |=| |\n         | | |\n |___  __  |_|\n  |@|      | |\n___________|_|_",

    10: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /        | |\n | U       |-|\n |       |=| |\n         | | |\n |_    __  |_|\n           | |\n___________|_|_",
}

regular_pics = {
    0: "           ___\n     |     | |\n    / \    | |\n   |--o|===|-|\n   |---|   | |\n  /     \  | |\n | U     | |-|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    1: "           ___\n           | |\n           | |\n      o|===|-|\n   |---|   | |\n  /     \  | |\n | U     | |-|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    2: "           ___\n           | |\n           | |\n        ===|-|\n    ---|   | |\n  /     \  | |\n | U     | |-|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    3: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /        | |\n | U     | |-|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    4: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /        | |\n | U       |-|\n |       |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    5: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /        | |\n | U       |-|\n |       |=| |\n         | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    6: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /        | |\n | U       |-|\n |       |=| |\n         | | |\n |___  __  |_|\n  |@| |@|  | |\n___________|_|_",

    7: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /        | |\n | U       |-|\n |       |=| |\n         | | |\n |___  __  |_|\n  |@|      | |\n___________|_|_",

    8: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /        | |\n | U       |-|\n |       |=| |\n         | | |\n |_    __  |_|\n           | |\n___________|_|_",
}

hard_pics = {
    0: "           ___\n     |     | |\n    / \    | |\n   |--o|===|-|\n   |---|   | |\n  /     \  | |\n | U     | |-|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    1: "           ___\n           | |\n           | |\n      o|===|-|\n   |---|   | |\n  /     \  | |\n | U     | |-|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    2: "           ___\n           | |\n           | |\n        ===|-|\n    ---|   | |\n  /     \  | |\n | U     | |-|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    3: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /        | |\n | U     | |-|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    4: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /        | |\n | U       |-|\n |       |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    5: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /        | |\n | U       |-|\n |       |=| |\n         | | |\n |___  __  |_|\n  |@|      | |\n___________|_|_",

    6: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /        | |\n | U       |-|\n |       |=| |\n         | | |\n |_    __  |_|\n           | |\n___________|_|_",
}

xtra_hard_pics = {
    0: "           ___\n     |     | |\n    / \    | |\n   |--o|===|-|\n   |---|   | |\n  /     \  | |\n | U     | |-|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    1: "           ___\n           | |\n           | |\n        ===|-|\n    ---|   | |\n  /     \  | |\n | U     | |-|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    2: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /        | |\n | U     | |-|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    3: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /        | |\n | U       |-|\n |       |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    4: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /        | |\n | U       |-|\n |       |=| |\n         | | |\n |___  __  |_|\n  |@|      | |\n___________|_|_",

    5: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /        | |\n | U       |-|\n |       |=| |\n         | | |\n |_    __  |_|\n           | |\n___________|_|_",
}

impossible_pics = {
    0: "           ___\n     |     | |\n    / \    | |\n   |--o|===|-|\n   |---|   | |\n  /     \  | |\n | U     | |-|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    1: "           ___\n           | |\n           | |\n        ===|-|\n    ---|   | |\n  /     \  | |\n | U     | |-|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_",

    2: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /        | |\n | U       |-|\n |       |=| |\n         | | |\n |__   __  |_|\n  |@|      | |\n___________|_|_",

    3: "           ___\n           | |\n           | |\n        ===|-|\n           | |\n  /        | |\n | U       |-|\n |       |=| |\n         | | |\n |_    __  |_|\n           | |\n___________|_|_",
}

difficulty_lives = {
    'very easy': 15,
    'easy': 12,
    'medium': 10,
    'regular': 8,
    'hard': 6,
    'xtra hard': 5,
    'impossible': 3
}

length_ranges = {
    'Xtreme': (20, 22),
    'Greater': (17, 19),
    'Longer': (13, 16),
    'Regular': (9, 12),
    'Small': (5, 8),
    'Mini': (2, 4)
}

texture1 = {
    0: '_|_     _|_     _|_     _|_     _|_     _|_     _|_     _|_     _|_    ',
    1: ' |       |       |       |       |       |       |       |       |     ',
    2: '    _|_     _|_     _|_     _|_     _|_     _|_     _|_     _|_     _|_',
    3: '     |       |       |       |       |       |       |       |       | ',
    # 4: '_|_     _|_     _|_     _|_     _|_     _|_     _|_',
    # 5: ' |       |       |       |       |       |       | ',
    # 6: '    _|_     _|_     _|_     _|_     _|_     _|_    ',
    # 7: '     |       |       |       |       |       |     ',
    # 8: '_|_     _|_     _|_     _|_     _|_     _|_     _|_',
    # 9: ' |       |       |       |       |       |       | ',
    # 10: '    _|_     _|_     _|_     _|_     _|_     _|_    ',
    # 11: '     |       |       |       |       |       |     '
}

texture2 = {
    0: '_|___|___|___|___|___|___|___|___|___|___|___|___|',
    1: '___|___|___|___|___|___|___|___|___|___|___|___|__',
    2: '_|___|___|___|___|___|___|___|___|___|___|___|___|',
    3: '___|___|___|___|___|___|___|___|___|___|___|___|__',
    4: '_|___|___|___|___|___|___|___|___|___|___|___|___|',
    5: '___|___|___|___|___|___|___|___|___|___|___|___|__',
    6: '_|___|___|___|___|___|___|___|___|___|___|___|___|',
    7: '___|___|___|___|___|___|___|___|___|___|___|___|__',
    8: '_|___|___|___|___|___|___|___|___|___|___|___|___|',
    9: '___|___|___|___|___|___|___|___|___|___|___|___|__',
    10: '_|___|___|___|___|___|___|___|___|___|___|___|___|',
    11: '___|___|___|___|___|___|___|___|___|___|___|___|__'
}

texture3 = {
    0: '         *                 *                  *              *        ',
    1: '                *                                     *          *    ',
    2: '                        *            *                             ___',
    3: '  *               *                                          |     | |',
    4: '        *              _________##                 *        / \    | |',
    5: '                      @\_\_\_\_\##    *     |              |--o|===|-|',
    6: '  *                  @@@_\_\_\_\##\       \|/|/            |---|   | |',
    7: '                    @@ @@\_\_\_\_\_\    \|\ |//|/     *   /     \  | |',
    8: '             *     @@@@@@@ _\_\_\_\_\     \|\|/|/        |  U    | |-|',
    9: '                  @@@@@@@@@----------|    \ |//          |  S    |=| |',
    10: '       __         @@ @@@ @@_|_|__|_|_|     \|/           |  A    | | |',
    11: '  ____|_@|_       @@@@@@@@@__________|     \|/           |_______| |_|',
    12: '=|__ _____ |=     @@@@ .@@@___|_|____|      |             |@| |@|  | |',
    13: '____0_____0__\|/__@@@@__@@@__________|_\|/__|___\|/__\|/___________|_|_'
}

takeoff_img = {
    0: '                                                   ,: ',
    1: '                                                 ," | ',
    2: "                                                /   : ",
    3: "                                             --'   /  ",
    4: '                                             \/ />/   ',
    5: '                                             / <//_\  ',
    6: '                                          __/   /     ',
    7: "                                          )'-. /      ",
    8: '                                          ./  :\      ',
    9: '                                           /.' '      ',
    10: "                                         '/'         ",
    11: '                                         +           ',
    12: '                                        "            ',
    13: '                                      `.             ',
    14: '                                  .-"-               ',
    15: '                                 (    |              ',
    16: '                             . .-'  '.               ',
    17: '                             ( (.   )8:              ',
    18: "                         .'    / (_  )               ",
    19: '                          _. :(.   )8P  `            ',
    20: "                      .  (  `-' (  `.   .            ",
    21: '                       .  :  (   .a8a)               ',
    22: '                      /_`( "a `a. )"`                ',
    23: "                  (  (/  .  ' )=='                   ",
    24: '                 (   (    )  .8"   +                 ',
    25: "                   (`'8a.( _(   (                    ",
    26: '                ..-. `8P    ) `  )  +                ',
    27: "              -'   (      -ab:  )                    ",
    28: '             "   _  "    (8P"Ya                      ',
    29: '          _(    (    )b  -`.  ) +                    ',
    30: '         ( 8)  ( _.aP" _a   \( \   *                 ',
    31: '       +  )/    (8P   (88    )  )                    ',
    32: '          (a:f   "     `"       `                    '
}


def set_music_volume():
    while True:
        volume_input = input("Enter volume value (0.0 - 1.0): ")

        try:
            volume = float(volume_input)
            if 0.0 <= volume <= 1.0:
                pygame.mixer.music.set_volume(volume)
                sleep('...')
                print(f"Volume set to {Fore.GREEN}{volume}{Fore.WHITE}")
                return
            else:
                sleep('...')
                invalid_text = pyfiglet.figlet_format(
                    text='IVALID', font='small')
                print(f'{Fore.GREEN}{invalid_text}')
                print("Please enter a value between 0.0 and 1.0.")
                sleep('...')
        except ValueError:
            sleep('...')
            invalid_text = pyfiglet.figlet_format(
                text='IVALID', font='small')
            print(f'{Fore.GREEN}{invalid_text}')
            print(f"{Fore.RED}'VALUE ERROR'{Fore.WHITE}")
            sleep('...')


def print_texture(texture):
    for line_number in texture:
        print(texture[line_number])


def sleep(text=None):
    if text is None:
        time.sleep(.5)
        print()
    else:
        time.sleep(.2)
        print(f'\n{text}\n')
        time.sleep(.3)


def format_time(seconds):
    minutes = int(seconds // 60)
    remaining_seconds = int(seconds % 60)
    formatted_time = f"{minutes} minutes and {remaining_seconds} seconds"
    return formatted_time


def select_word(filename, word_length_setting):
    min_length, max_length = length_ranges[word_length_setting]
    with open(filename, 'r') as file:
        file = file.read()
    words_list = file.split()
    filtered_words = [
        word for word in words_list if min_length <= len(word) <= max_length]  # list comprehension, very cool!
    launch_code = random.choice(filtered_words)
    return launch_code


def load_game_number():
    with open('game_number.txt', 'r') as file:
        return int(file.read().strip())


def save_game_number(game_number):
    with open('game_number.txt', 'w') as file:
        file.write(str(game_number) + '\n')


def load_game_difficulty():
    with open('game_difficulty.txt', 'r') as file:
        return str(file.read().strip())


def save_game_difficulty(game_difficulty):
    with open('game_difficulty.txt', 'w') as file:
        file.write(str(game_difficulty) + '\n')


def load_word_length():
    with open('word_length.txt', 'r') as file:
        return str(file.read().strip())


def save_word_length(word_length):
    with open('word_length.txt', 'w') as file:
        file.write(str(word_length) + '\n')


def load_score_history():
    with open("score_history.txt", 'r') as score_history:
        return json.load(score_history)


def save_score_history(score_history):
    with open('score_history.txt', 'w') as file:
        json.dump(score_history, file)


def load_high_score():
    with open('high_score.txt', 'r') as file:
        return float(file.read().strip())


def save_high_score(high_score):
    with open('high_score.txt', 'w') as file:
        file.write(str(high_score) + '\n')


def print_starman_progression(game_difficulty):
    if game_difficulty == 'Very Easy':
        for step in very_easy_pics:
            print(f'\nWrong Guess {Fore.CYAN}{step}{Fore.WHITE}:\n')
            print(f'{Fore.YELLOW}{very_easy_pics[step]}\n \n')
            time.sleep(.5)
    elif game_difficulty == 'Easy':
        for step in easy_pics:
            print(f'\nWrong Guess {Fore.CYAN}{step}{Fore.WHITE}:\n')
            print(f'{Fore.YELLOW}{easy_pics[step]}\n \n')
            time.sleep(.5)
    elif game_difficulty == 'Medium':
        for step in medium_pics:
            print(f'\nWrong Guess {Fore.CYAN}{step}{Fore.WHITE}:\n')
            print(f'{Fore.YELLOW}{medium_pics[step]}\n \n')
            time.sleep(.5)
    elif game_difficulty == 'Regular':
        for step in regular_pics:
            print(f'\nWrong Guess {Fore.CYAN}{step}{Fore.WHITE}:\n')
            print(f'{Fore.YELLOW}{regular_pics[step]}\n \n')
            time.sleep(.5)
    elif game_difficulty == 'Hard':
        for step in hard_pics:
            print(f'\nWrong Guess {Fore.CYAN}{step}{Fore.WHITE}:\n')
            print(f'{Fore.YELLOW}{hard_pics[step]}\n \n')
            time.sleep(.5)
    elif game_difficulty == 'Xtra Hard':
        for step in xtra_hard_pics:
            print(f'\nWrong Guess {Fore.CYAN}{step}{Fore.WHITE}:\n')
            print(f'{Fore.YELLOW}{xtra_hard_pics[step]}\n \n')
            time.sleep(.5)
    elif game_difficulty == 'Impossible':
        for step in impossible_pics:
            print(f'\nWrong Guess {Fore.CYAN}{step}{Fore.WHITE}:\n')
            print(f'{Fore.YELLOW}{impossible_pics[step]}\n \n')
            time.sleep(.5)


def test_fonts(text):
    with open('pyfigletfonts.txt', 'r') as file:
        fonts = file.read().splitlines()

    for font_example in fonts:
        print(f'Testing font {Fore.CYAN}{font_example}{Fore.WHITE}:\n')
        test_font = pyfiglet.figlet_format(text=f'{text}', font=font_example)
        print()
        print(test_font)
        print(f'\n')
        time.sleep(.008)


def count_words_by_length(filename):
    word_counts = {}

    try:
        with open(filename, 'r') as file:
            for line in file:
                word = line.strip()
                length = len(word)
                if length not in word_counts:
                    word_counts[length] = 0
                word_counts[length] += 1
    except FileNotFoundError:
        print("File not found.")
        return []

    sorted_counts = sorted(word_counts.items(), reverse=True)
    result = [f"{length} letter words: {count}" for length,
              count in sorted_counts]
    return result


def display_letters(word, guessed_letters, game_difficulty, wrong_guesses):
    if game_difficulty == 'Very Easy':
        print(f'{Fore.YELLOW}{very_easy_pics[wrong_guesses]}')
    elif game_difficulty == 'Easy':
        print(f'{Fore.YELLOW}{easy_pics[wrong_guesses]}')
    elif game_difficulty == 'Medium':
        print(f'{Fore.YELLOW}{medium_pics[wrong_guesses]}')
    elif game_difficulty == 'Regular':
        print(f'{Fore.YELLOW}{regular_pics[wrong_guesses]}')
    elif game_difficulty == 'Hard':
        print(f'{Fore.YELLOW}{hard_pics[wrong_guesses]}')
    elif game_difficulty == 'Xtra Hard':
        print(f'{Fore.YELLOW}{xtra_hard_pics[wrong_guesses]}')
    elif game_difficulty == 'Impossible':
        print(f'{Fore.YELLOW}{impossible_pics[wrong_guesses]}')
    print()
    print(f'\n \n{Fore.CYAN}Launch Code{Fore.WHITE}: ')
    chosen_word = ''
    for letter in word:
        if letter.upper() in guessed_letters:
            chosen_word += letter.lower() + ' '
        else:
            chosen_word += '_ '
    if chosen_word:
        chosen_word = chosen_word[0].upper() + chosen_word[1:]
    return chosen_word


def user_guess(counter, guessed_letters, launch_code, display, game_difficulty):
    while counter > 0:
        if counter == difficulty_lives[game_difficulty.lower()] and len(guessed_letters) == 0:
            print(
                f'You have {Fore.GREEN}{counter}{Fore.WHITE} guesses remaining!!')
        if counter < difficulty_lives[game_difficulty.lower()] and counter > 3:
            print(
                f'You only have {Fore.GREEN}{counter}{Fore.WHITE} wrong attempts remaining!!')
        if counter == 1:
            print(
                f'Last chance!! You only have {Fore.RED}{counter}{Fore.WHITE} engine remaining!!')
        if counter == difficulty_lives[game_difficulty.lower()] and len(guessed_letters) > 0:
            print(
                f'You still have {Fore.GREEN}{counter}{Fore.WHITE} wrong attempts remaining!!')
        if counter > 1 and counter < 4 and len(guessed_letters) > 0:
            print(
                f'Watch out!! You only have {Fore.RED}{counter}{Fore.WHITE} wrong attempts remaining!!')

        formatted_multi_guesses = ', '.join(
            guessed_letters[:-1]) + ' & ' + guessed_letters[-1] if len(guessed_letters) > 1 else ''
        formatted_guesses = ', '.join(guessed_letters) if len(
            guessed_letters) == 1 else ''

        if formatted_guesses:
            print(f'So far you have guessed: {formatted_guesses}')
        if formatted_multi_guesses:
            print(f'So far you have guessed: {formatted_multi_guesses}')

        print()  # aesthetic empty line

        guess = input('Guess a letter: > ').lower().strip()
        sleep('...')

        if guess.lower() == 'ex':
            exiting_game_text = pyfiglet.figlet_format(
                text="EXITING GAME", font='smslant')
            print(exiting_game_text)
            # print('//EXITING CURRENT GAME//')
            sleep('...')
            return None
        if guess.lower() == launch_code.lower():
            sleep('...')
            return guess
        elif guess.lower() == 'vol':
            sleep('...')
            set_music_volume()
            sleep('...')
        elif len(guess) > 1:
            print('Please enter only (1) letter at a time!')
            sleep('...')
            print(f'\n{display}\n')
        if not guess.isalpha():
            print('Please enter only a letter!')
            sleep('...')
            print(f'\n{display}\n')
        elif guess.upper() in guessed_letters and guess.upper() != 'F':
            print(f'You have already guessed: {guess}\n')
            sleep('...')
            print(f'\n{display}\n')
        elif guess.upper() == 'F' and guess.upper() in guessed_letters:
            f_pressed_text = pyfiglet.figlet_format(
                text="'F' PRESSED", font="standard", width=50)
            print(f_pressed_text)
            print("\nYou have paid respects.\nPlease guess again.")
            sleep('...')
        elif guess in launch_code and guess not in guessed_letters:
            return guess

        else:
            return guess[0]


def play_game(filename, score_history, high_score, word_length_setting, game_difficulty):
    play = True
    game_number = load_game_number()
    high_score = load_high_score()
    wrong_guesses = 0

    congrats_statements = [
        "Great job!",
        "Well done!",
        "You're a genius!",
        "You're on fire!",
        "Fantastic guess!",
        "Incredible!",
        "Impressive work!",
        "You nailed it!",
        "You're a word wizard!",
        "You're unstoppable!",
        "Bravo!",
        "You're amazing!",
        "You've got this down!",
        "Outstanding!",
        "You're a pro!",
        "Spectacular!",
        "You're on a roll!",
        "You're killing it!",
        "You're a master of this!",
        "You're the word detective!",
        "You're rocking it!",
        "Terrific job!",
        "You're a word expert!",
        "You're making it look easy!",
        "Way to go!",
        "You're getting closer!",
        "You're spot on!",
        "Excellent guess!",
        "You're on the mark!",
        "You're a word champion!"
    ]

    dissapoint_statements = [
        "Oh No!",
        "I'm so sorry!",
        "Ooops, wrong guess!",
        "Better luck next time!",
        "Oh no, that's not correct!",
        "Keep trying!",
        "Don't worry, you'll get one soon enough!",
        "Not quite right.",
        "Almost there, but not quite.",
        "You're on the right track!",
        "Not the letter we're looking for.",
        "Try a different letter.",
        "You're so close!",
        "The launch code isn't that.",
        "That's not the missing piece.",
        "It's not that letter.",
        "Keep searching, you'll find it!"
    ]

    win_statements = [
        "You're literally the smartest person ever!!",
        "OMG how'd you do that?! You're amazing!!",
        "You made this game look so easy!!",
        "You've cracked the code like a master detective!",
        "Congratulations, word wizard! You've triumphed!",
        "Bravo! You've emerged victorious as the word master!",
        "Incredible job! You've conquered the word challenge!",
        "You've shown unparalleled skill in solving mysteries of words!"
    ]

    record_statements = [
        "Excellent Job!",
        "You've made it look easy!",
        "You're amazing!",
        "You're unstoppable!",
        "What a beast!",
        "You're a word guessing god!",
        "All hail the word master!",
    ]

    length_ranges = {
        'Xtreme': (20, 22),
        'Greater': (17, 19),
        'Longer': (13, 16),
        'Regular': (9, 12),
        'Small': (5, 8),
        'Mini': (2, 4)
    }

    print(
        f'\nShucks! We forgot the {Fore.CYAN}launch code{Fore.WHITE} again!\nHelp mission control decode the data before your rocket completely falls apart!\n')
    score_time = format_time(high_score)

    while play:
        pygame.mixer.music.stop()
        pygame.mixer.music.load(game_music_path)
        pygame.mixer.music.play(-1)
        print(
            f'Out of {Fore.CYAN}{game_number}{Fore.WHITE} games played, your fastest time is:\n')

        print(f'{Fore.GREEN}{score_time}\n')

        print('Can you set a new record??\nYour current settings are: \n')

        if word_length_setting.lower() == 'mini':
            print(
                f'Word Length: {Back.BLUE}{word_length_setting}{Back.BLACK}')
        if word_length_setting.lower() == 'small' or word_length_setting.lower() == 'regular':
            print(
                f'Word Length: {Back.GREEN}{Fore.BLACK}{word_length_setting}{Back.BLACK}{Fore.WHITE}')
        if word_length_setting.lower() == 'longer':
            print(
                f'Word Length: {Back.YELLOW}{Fore.BLACK}{word_length_setting}{Back.BLACK}{Fore.WHITE}')
        if word_length_setting.lower() == 'greater' or word_length_setting.lower() == 'xtreme':
            print(
                f'Word Length: {Back.RED}{word_length_setting}{Back.BLACK}')

        # print(f'Word Length: {Back.BLUE}{Fore.WHITE}{word_length_setting}{Back.BLACK}{Fore.YELLOW}')

        if game_difficulty.lower() == 'very easy' or game_difficulty.lower() == 'easy':
            print(
                f'Game Difficulty: {Back.GREEN}{game_difficulty}{Back.BLACK}\n')
        if game_difficulty.lower() == 'medium' or game_difficulty.lower() == 'regular':
            print(
                f'Game Difficulty: {Back.BLUE}{game_difficulty}{Back.BLACK}\n')
        if game_difficulty.lower() == 'hard':
            print(
                f'Game Difficulty: {Back.YELLOW}{game_difficulty}{Back.BLACK}\n')
        if game_difficulty.lower() == 'xtra hard' or game_difficulty.lower() == 'impossible':
            print(
                f'Game Difficulty: {Back.RED}{game_difficulty}{Back.BLACK}\n')

        # print(f'Game Difficulty: {Back.RED}{game_difficulty}{Back.BLACK}\n')

        print(
            f'These settings will generate words with {Fore.CYAN}{length_ranges[word_length_setting][0]}{Fore.WHITE} to {Fore.CYAN}{length_ranges[word_length_setting][1]}{Fore.WHITE} letters.\nYou are given {Fore.GREEN}{difficulty_lives[game_difficulty.lower()]}{Fore.WHITE} wrong guesses before {Fore.RED}MISSION FAILURE.{Fore.WHITE}\n[EX]it to return to {Fore.MAGENTA}Mission Control{Fore.WHITE} or reset the game.')

        sleep()

        # game_number += 1
        # save_game_number(game_number)
        launch_code = select_word(filename, word_length_setting)
        guessed_letters = []
        counter = difficulty_lives[game_difficulty.lower()]

        start_time = time.time()  # record the start time

        # print(launch_code)
        print()

        while counter > 0:
            display = display_letters(
                launch_code, guessed_letters, game_difficulty, wrong_guesses)
            print(f'\n{display}\n')

            if '_ ' not in display:
                pygame.mixer.music.stop()
                pygame.mixer.music.load(victory_music_path)
                pygame.mixer.music.play(-1)
                # displays victory screen, press 'Q' to quit
                start_screen()
                end_time = time.time()  # Record the end time
                duration = end_time - start_time
                formatted_time = format_time(duration)
                formatted_word = launch_code[0].upper(
                ) + launch_code[1:].lower()
                win_message = random.choice(win_statements)
                win_text = pyfiglet.figlet_format(
                    text="LIFT OFF", font="isometric1")
                print_texture(takeoff_img)
                time.sleep(.5)
                print(f'\n{win_text}')
                time.sleep(2)
                print(
                    f"{win_message}\nYou guessed the launch code, {Fore.CYAN}'{formatted_word}'{Fore.WHITE}!\nYou successfully launched into outer space!")
                print(
                    f'It only took you {Fore.GREEN}{formatted_time}{Fore.WHITE}!')
                print('...')

                if high_score is None:
                    high_score = duration
                    record_message = random.choice(record_statements)
                    record_text = pyfiglet.figlet_format(
                        text="New Record", font='puffy')
                    print(record_text)
                    print(
                        f"{record_message} You've just set your first record!\nCheck out 'High Score' to view your fastest time!")
                elif high_score is not None and duration < high_score:
                    high_score = duration
                    save_high_score(high_score)
                    record_message = random.choice(record_statements)
                    record_text = pyfiglet.figlet_format(
                        text="New Record", font='puffy')
                    print(record_text)
                    print(
                        f"{record_message} You just set a {Fore.GREEN}*NEW*{Fore.WHITE} record!\n'High Score' has been updated with your latest time!")

                # adding to score history dictionary
                game_number += 1
                save_game_number(game_number)
                score_history[f'Game {game_number}'] = f'WIN - Length: {word_length_setting}, Difficulty: {game_difficulty}, {launch_code}, {formatted_time}'
                with open('score_history.txt', 'w') as file:
                    json.dump(score_history, file)

                sleep('...')
                break

            eftiwall_font = pyfiglet.figlet_format(
                text='9( ajy', font='eftiwall')
            print(f'\n{eftiwall_font}')
            guess = user_guess(counter, guessed_letters,
                               launch_code, display, game_difficulty)

            if guess is None:
                end_time = time.time()  # Record the end time
                duration = end_time - start_time
                formatted_time = format_time(duration)
                game_number += 1
                save_game_number(game_number)
                score_history[f'Game {game_number}'] = f'EXIT - Length: {word_length_setting}, Difficulty: {game_difficulty}, {launch_code}, {formatted_time}'
                with open('score_history.txt', 'w') as file:
                    json.dump(score_history, file)
                play = False
                break

            if guess in launch_code and guess.upper() not in guessed_letters:
                congrats_message = random.choice(congrats_statements)
                print(
                    f'{congrats_message} You guessed "{guess.upper()}" {Fore.GREEN}correctly{Fore.WHITE}!')
                sleep('...')
                guessed_letters.append(guess.upper())

            if guess not in launch_code and guess not in guessed_letters:
                dissapoint_message = random.choice(dissapoint_statements)
                print(
                    f"{dissapoint_message} '{guess.upper()}' is {Fore.RED}not{Fore.WHITE} in the launch code :(")
                sleep('...')
                guessed_letters.append(guess.upper())
                counter -= 1
                wrong_guesses += 1

        else:
            end_time = time.time()  # Record the end time
            duration = end_time - start_time
            formatted_time = format_time(duration)
            pygame.mixer.music.stop()
            pygame.mixer.music.load(gameover_music_path)
            pygame.mixer.music.play()
            start_screen1()
            display = display_letters(
                launch_code, guessed_letters, game_difficulty, wrong_guesses)
            formatted_word = launch_code[0].upper(
            ) + launch_code[1:].lower()
            print(f'\n{display}\n')
            game_over_text = pyfiglet.figlet_format(
                text='GAME OVER', font='poison')
            print(game_over_text)
            print(
                f'\n{Fore.RED}MISSION FAILURE{Fore.WHITE}:\nThe launch code was: {Fore.CYAN}{formatted_word}{Fore.WHITE}\nYour rocket fell apart on the launch pad :(')
            print(f'You played for: {Fore.RED}{formatted_time}{Fore.WHITE}')
            sleep('...')
            # adding to score history dictionary
            game_number += 1
            save_game_number(game_number)
            score_history[f'Game {game_number}'] = f'LOSS - Length: {word_length_setting}, Difficulty: {game_difficulty}, {launch_code}, {formatted_time}'
            with open('score_history.txt', 'w') as file:
                json.dump(score_history, file)

        while True:
            play_again = input(
                'Do you want to play again? (y/n) > ').lower().strip()
            sleep('...')
            if play_again.lower() == 'n':
                thanks_text = pyfiglet.figlet_format(
                    text="Thanks For Playing", font="speed")
                print(thanks_text)
                # print('Thanks for playing!')
                play = False
                break
            if play_again.upper() == 'F':
                f_pressed_text = pyfiglet.figlet_format(
                    text="'F' PRESSED", font="standard", width=50)
                print(f_pressed_text)
                print(
                    "\nYou have paid respects.\nPlease enter 'yes' or 'no'.")
                sleep('...')
            elif play_again.lower() == 'y':
                play = True
                pygame.mixer.music.stop()
                pygame.mixer.music.load(countdown_music_path)
                pygame.mixer.music.play(-1)
                resetting_game_text = pyfiglet.figlet_format(
                    text="RESETTING GAME", font='smslant')
                print(resetting_game_text)
                # print('//RESETTING GAME//')
                sleep('...')
                three_text = pyfiglet.figlet_format(
                    text='Three', font='rowancap')
                print(three_text)
                sleep('...')
                two_text = pyfiglet.figlet_format(
                    text='TWO', font='nancyj-fancy')
                print(two_text)
                sleep('...')
                one_text = pyfiglet.figlet_format(text='ONE!', font='roman')
                print(one_text)
                sleep('...')
                ready_text = pyfiglet.figlet_format(
                    text='Ready!', font='eca_____')
                print(f'{ready_text}')
                sleep('...')
                print_texture(texture1)
                print()
                eftiwall_font = pyfiglet.figlet_format(
                    text='9( ajy', font='eftiwall')
                print(f'{eftiwall_font}')
                # print('\n \nReady to go!!')
                counter = difficulty_lives[game_difficulty.lower()]
                guessed_letters = []
                wrong_guesses = 0
                break
            else:
                invalid_text = pyfiglet.figlet_format(
                    text='IVALID', font='small')
                print(f'{Fore.RED}{invalid_text}')
                print("Please enter either 'yes' or 'no'")
                sleep('...')
        if not play:
            return high_score


def main_menu():
    filename = 'words.txt'
    score_history = load_score_history()
    high_score = load_high_score()
    word_length_setting = load_word_length()
    game_difficulty = load_game_difficulty()
    # print('\nWelcome to starman!\n')
    welcome_to_text = pyfiglet.figlet_format(
        text='Welcome to', font='rectangles')
    print(welcome_to_text)
    time.sleep(.5)
    game_name_text = pyfiglet.figlet_format(text="Starman!",
                                            font="slant",)
    print(f'{Fore.YELLOW}{game_name_text}')
    time.sleep(.5)
    print()
    print_texture(texture3)
    time.sleep(1)
    print('\n')
    while True:
        pygame.mixer.music.stop()
        pygame.mixer.music.load(menu_music_path)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

        print_texture(texture1)
        print()
        eftiwall_font = pyfiglet.figlet_format(text='9( ajy', font='eftiwall')
        print(f'{eftiwall_font}')
        menu_text = pyfiglet.figlet_format(
            text='Mission Control', font='small')
        print(
            f"{menu_text}\nOptions:\n[P]lay the game\n[L]ift off\n[C]heck high score\n[V]iew score history\n[S]ettings\n[T]ools\n[E]xit the game\n")

        choice = input('Choose an option: > ').lower().strip()

        if choice.lower() == 'vol':
            sleep('...')
            set_music_volume()
            sleep('...')

        if choice == 'p':
            sleep('...')
            initializing_game_text = pyfiglet.figlet_format(
                text="STARTING GAME!", font='smslant')
            print(initializing_game_text)
            sleep('...')
            print_texture(texture1)
            new_high_score = play_game(
                filename, score_history, high_score, word_length_setting, game_difficulty)
            save_high_score(new_high_score)
            sleep('...')

        if choice == 'l':
            sleep('...')
            win_text = pyfiglet.figlet_format(
                text="LIFT OFF", font="isometric1")
            print_texture(takeoff_img)
            time.sleep(.5)
            print(f'\n{win_text}')
            time.sleep(2)
            sleep('...')

        elif choice == 'c':
            sleep('...')
            if high_score is None:
                print('No record has been set yet.')
            else:
                formatted_time = format_time(high_score)
                # print(high_score)
                print(f'The current record is: \n{Fore.GREEN}{formatted_time}')
            sleep('...')

        elif choice == 'v':
            sleep('...')
            initializing_score_history = pyfiglet.figlet_format(
                text="--SCORE HISTORY--", font='smslant')
            print(initializing_score_history)
            for game, duration in score_history.items():
                print(f"{game}: {duration}")
            print("\n--- End of Score History ---")
            sleep('...')

        elif choice == 's':
            game_setting_flag = True
            sleep('...')
            game_settings_text = pyfiglet.figlet_format(
                text="GAME SETTINGS", font='smslant')
            print(game_settings_text)
            # print('//GAME SETTINGS//')
            sleep('...')
            print(
                'Options:\n[L]ength setting\n[D]ifficulty setting\n[E]xit\n')
            while game_setting_flag:
                setting_choice = input('Select an option: > ').lower().strip()

                if setting_choice == 'l':
                    choice_flag = True
                    sleep('...')
                    length_settings_text = pyfiglet.figlet_format(
                        text="LENGTH SETTINGS", font='smslant')
                    print(length_settings_text)
                    # print('//WORD LENGTH SETTINGS//')
                    sleep('...')
                    print(
                        f'Word Lengths:\n[X]treme  | (20-22 letters)\n[G]reater | (17-19 letters)\n[L]onger  | (13-16 letters)\n[R]egular | (9-12 letters)\n[S]mall   | (5-8 letters)\n[M]ini    | (2-4 letters)\n \n \nThe word length is currently set to: \n \n')

                    if word_length_setting.lower() == 'mini':
                        print(
                            f'{Back.BLUE}{Fore.WHITE}{word_length_setting}{Fore.WHITE}{Back.BLACK} ({Fore.CYAN}{length_ranges[word_length_setting][0]}{Fore.WHITE}-{Fore.CYAN}{length_ranges[word_length_setting][1]}{Fore.WHITE} letters)\n')

                    if word_length_setting.lower() == 'small' or word_length_setting.lower() == 'regular':
                        print(
                            f'{Back.GREEN}{Fore.BLACK}{word_length_setting}{Fore.WHITE}{Back.BLACK} ({Fore.CYAN}{length_ranges[word_length_setting][0]}{Fore.WHITE}-{Fore.CYAN}{length_ranges[word_length_setting][1]}{Fore.WHITE} letters)\n')

                    if word_length_setting.lower() == 'longer':
                        print(
                            f'{Back.YELLOW}{Fore.BLACK}{word_length_setting}{Fore.WHITE}{Back.BLACK} ({Fore.CYAN}{length_ranges[word_length_setting][0]}{Fore.WHITE}-{Fore.CYAN}{length_ranges[word_length_setting][1]}{Fore.WHITE} letters)\n')

                    if word_length_setting.lower() == 'greater' or word_length_setting.lower() == 'xtreme':
                        print(
                            f'{Back.RED}{Fore.WHITE}{word_length_setting}{Fore.WHITE}{Back.BLACK} ({Fore.CYAN}{length_ranges[word_length_setting][0]}{Fore.WHITE}-{Fore.CYAN}{length_ranges[word_length_setting][1]}{Fore.WHITE} letters)\n')

                    # {Fore.WHITE}{Back.BLUE}{word_length_setting}{Fore.WHITE}{Back.BLACK}

                    while choice_flag:
                        maybe_change = input(
                            'Would you like to change the word length? (y/n) > ').lower().strip()
                        if maybe_change == 'y':
                            sleep('...')
                            while True:
                                len_change = input(
                                    'Select new word length: > ').lower().strip()

                                if len_change.lower() == 'vol':
                                    sleep('...')
                                    set_music_volume()
                                    sleep('...')

                                if len_change == 'x':
                                    sleep('...')
                                    word_length_setting = 'Xtreme'
                                    save_word_length(word_length_setting)
                                    choice_flag = False
                                    print(
                                        f'The Word Length Setting has been set to: \n \n{Fore.RED}{word_length_setting}')
                                    sleep('...')
                                    game_setting_flag = False
                                    break

                                elif len_change == 'g':
                                    sleep('...')
                                    word_length_setting = 'Greater'
                                    save_word_length(word_length_setting)
                                    choice_flag = False
                                    print(
                                        f'The Word Length Setting has been set to: \n \n{Fore.RED}{word_length_setting}')
                                    sleep('...')
                                    game_setting_flag = False
                                    break

                                elif len_change == 'l':
                                    sleep('...')
                                    word_length_setting = 'Longer'
                                    save_word_length(word_length_setting)
                                    choice_flag = False
                                    print(
                                        f'The Word Length Setting has been set to: \n \n{Fore.YELLOW}{word_length_setting}')
                                    sleep('...')
                                    game_setting_flag = False
                                    break

                                elif len_change == 'r':
                                    sleep('...')
                                    word_length_setting = 'Regular'
                                    save_word_length(word_length_setting)
                                    choice_flag = False
                                    print(
                                        f'The Word Length Setting has been set to: \n \n{Fore.GREEN}{word_length_setting}')
                                    sleep('...')
                                    game_setting_flag = False
                                    break

                                elif len_change == 's':
                                    sleep('...')
                                    word_length_setting = 'Small'
                                    save_word_length(word_length_setting)
                                    choice_flag = False
                                    print(
                                        f'The Word Length Setting has been set to: \n \n{Fore.GREEN}{word_length_setting}')
                                    sleep('...')
                                    game_setting_flag = False
                                    break

                                elif len_change == 'm':
                                    sleep('...')
                                    word_length_setting = 'Mini'
                                    save_word_length(word_length_setting)
                                    choice_flag = False
                                    print(
                                        f'The Word Length Setting has been set to: \n \n{Fore.BLUE}{word_length_setting}')
                                    sleep('...')
                                    game_setting_flag = False
                                    break

                        elif maybe_change == 'n':
                            sleep('...')
                            return_menu_text = pyfiglet.figlet_format(
                                text="BACK TO MENU", font='rectangles')
                            print(return_menu_text)
                            # print('//RETURNING TO MENU//')
                            sleep('...')
                            game_setting_flag = False
                            break

                        elif maybe_change == 'f':
                            sleep('...')
                            f_pressed_text = pyfiglet.figlet_format(
                                text="'F' PRESSED", font="standard", width=50)
                            print(f_pressed_text)
                            print("\nYou have paid respects.")
                            sleep('...')

                        if maybe_change.lower() == 'vol':
                            sleep('...')
                            set_music_volume()
                            sleep('...')

                        else:
                            sleep('...')
                            invalid_text = pyfiglet.figlet_format(
                                text='IVALID', font='small')
                            print(f'{Fore.RED}{invalid_text}')
                            print(
                                f'Please choose (y/n)')
                            sleep('...')
                    break

                elif setting_choice == 'd':
                    setting_choice_flag = True
                    sleep('...')
                    difficulty_settings_text = pyfiglet.figlet_format(
                        text="DIFFICULTY SETTINGS", font='smslant')
                    print(difficulty_settings_text)
                    # print('//DIFFICULTY SETTINGS//')
                    sleep('...')
                    print(
                        f'Options:\n[V]ery Easy  | (15 Lives)\n[E]asy       | (12 Lives)\n[M]edium     | (10 Lives)\n[R]egular    | (8 Lives)\n[H]ard       | (6 Lives)\n[X]tra Hard  | (5 Lives)\n[I]mpossible | (3 Lives)\n \n \nThe difficutly is currently set to:\n \n')

                    if game_difficulty.lower() == 'very easy' or game_difficulty.lower() == 'easy':
                        print(
                            f'Game Difficulty: {Fore.WHITE}{Back.GREEN}{game_difficulty}{Fore.WHITE}{Back.BLACK}\n')
                    if game_difficulty.lower() == 'medium' or game_difficulty.lower() == 'regular':
                        print(
                            f'Game Difficulty: {Fore.WHITE}{Back.BLUE}{game_difficulty}{Fore.WHITE}{Back.BLACK}\n')
                    if game_difficulty.lower() == 'hard':
                        print(
                            f'Game Difficulty: {Fore.WHITE}{Back.YELLOW}{game_difficulty}{Fore.WHITE}{Back.BLACK}\n')
                    if game_difficulty.lower() == 'xtra hard' or game_difficulty.lower() == 'impossible':
                        print(
                            f'Game Difficulty: {Fore.WHITE}{Back.RED}{game_difficulty}{Fore.WHITE}{Back.BLACK}\n')

                    # print(f'{Fore.WHITE}{Back.RED}{game_difficulty}{Fore.WHITE}{Back.BLACK}\n')

                    while setting_choice_flag:
                        change_maybe = input(
                            'Would you like to change the game difficulty? (y/n) > ')

                        if change_maybe == 'y':
                            sleep('...')
                            while True:
                                change_diff = input(
                                    'Select new game difficulty: > ').lower().strip()

                                if choice.lower() == 'vol':
                                    sleep('...')
                                    set_music_volume()
                                    sleep('...')

                                if change_diff == 'v':
                                    sleep('...')
                                    game_difficulty = 'Very Easy'
                                    save_game_difficulty(game_difficulty)
                                    setting_choice_flag = False
                                    print(
                                        f'The game difficulty has been set to: \n \n{Fore.GREEN}{game_difficulty}')
                                    sleep('...')
                                    game_setting_flag = False
                                    break

                                elif change_diff == 'e':
                                    sleep('...')
                                    game_difficulty = 'Easy'
                                    save_game_difficulty(game_difficulty)
                                    setting_choice_flag = False
                                    print(
                                        f'The game difficulty has been set to: \n \n{Fore.GREEN}{game_difficulty}')
                                    sleep('...')
                                    game_setting_flag = False
                                    break

                                elif change_diff == 'm':
                                    sleep('...')
                                    game_difficulty = 'Medium'
                                    save_game_difficulty(game_difficulty)
                                    setting_choice_flag = False
                                    print(
                                        f'The game difficulty has been set to: \n \n{Fore.BLUE}{game_difficulty}')
                                    sleep('...')
                                    game_setting_flag = False
                                    break

                                elif change_diff == 'r':
                                    sleep('...')
                                    game_difficulty = 'Regular'
                                    save_game_difficulty(game_difficulty)
                                    setting_choice_flag = False
                                    print(
                                        f'The game difficulty has been set to: \n \n{Fore.BLUE}{game_difficulty}')
                                    sleep('...')
                                    game_setting_flag = False
                                    break

                                elif change_diff == 'h':
                                    sleep('...')
                                    game_difficulty = 'Hard'
                                    save_game_difficulty(game_difficulty)
                                    setting_choice_flag = False
                                    print(
                                        f'The game difficulty has been set to: \n \n{Fore.YELLOW}{game_difficulty}')
                                    sleep('...')
                                    game_setting_flag = False
                                    break

                                elif change_diff == 'x':
                                    sleep('...')
                                    game_difficulty = 'Xtra Hard'
                                    save_game_difficulty(game_difficulty)
                                    setting_choice_flag = False
                                    print(
                                        f'The game difficulty has been set to: \n \n{Fore.RED}{game_difficulty}')
                                    sleep('...')
                                    game_setting_flag = False
                                    break

                                elif change_diff == 'i':
                                    sleep('...')
                                    game_difficulty = 'Impossible'
                                    save_game_difficulty(game_difficulty)
                                    setting_choice_flag = False
                                    print(
                                        f'The game difficulty has been set to: \n \n{Fore.RED}{game_difficulty}')
                                    sleep('...')
                                    game_setting_flag = False
                                    break

                                else:
                                    sleep('...')
                                    invalid_text = pyfiglet.figlet_format(
                                        text='IVALID', font='small')
                                    print(f'{Fore.BLUE}{invalid_text}')
                                    print(
                                        "Please choose one of the options listed.")
                                    sleep('...')

                        elif change_maybe == 'n':
                            sleep('...')
                            return_menu_text = pyfiglet.figlet_format(
                                text="BACK TO MENU", font='rectangles')
                            print(return_menu_text)
                            # print('//RETURNING TO MENU//')
                            sleep('...')
                            setting_choice_flag = False
                            game_setting_flag = False
                            break

                        if change_maybe.lower() == 'vol':
                            sleep('...')
                            set_music_volume()
                            sleep('...')

                        else:
                            sleep('...')
                            invalid_text = pyfiglet.figlet_format(
                                text='IVALID', font='small')
                            print(f'{Fore.RED}{invalid_text}')
                            print(
                                f'Please choose (y/n)')
                            sleep('...')
                    break

                elif setting_choice == 'e':
                    sleep('...')
                    # print('//RETURNING TO MENU//')
                    return_menu_text = pyfiglet.figlet_format(
                        text="BACK TO MENU", font='rectangles')
                    print(return_menu_text)
                    sleep('...')
                    break

        elif choice == 'f':
            sleep('...')
            f_pressed_text = pyfiglet.figlet_format(
                text="'F' PRESSED", font="standard", width=50)
            print(f_pressed_text)
            print("\nYou have paid respects.")
            sleep('...')

        elif choice == 'e':
            sleep('...')
            print('\nThanks for playing!\nSee you again soon!\n')
            goodbye_text = pyfiglet.figlet_format(
                text='Goodbye!', font='larry3d')
            print(goodbye_text)
            break

        elif choice == 't':
            sleep('...')
            while True:
                dev_tool_text = pyfiglet.figlet_format(
                    text='DEV TOOLS', font='Rectangles', width=50)
                print(dev_tool_text)
                print(
                    '\n \nOptions:\n[L]engths of words listed\n[R]andom word generator\n[I]mage progression\n[F]ont Tester\n[E]xit\n \n')
                tool_choice = input(
                    'Choose an option: > ').lower().strip()

                if tool_choice == 'l':
                    sleep('...')
                    word_length_counts = count_words_by_length(filename)
                    print(
                        'The lengths of the words in this list & how numerous they are:\n')
                    for length_count in word_length_counts:
                        print(length_count)
                    sleep('...')

                elif tool_choice == 'r':
                    sleep('...')
                    random_word_generator = pyfiglet.figlet_format(
                        text="RANDOM WORD GENERATOR", font='smslant')
                    print(random_word_generator)
                    # print('//RANDOM WORD GENERATOR//')
                    random_word = select_word(filename, word_length_setting)
                    sleep('...')
                    print(f'Your current word length is:\n \n')

                    if word_length_setting.lower() == 'mini':
                        print(
                            f'Word Length:{Back.WHITE} {Fore.BLUE}{word_length_setting}{Fore.WHITE} {Back.BLACK}({Fore.CYAN}{length_ranges[word_length_setting][0]}{Fore.WHITE}-{Fore.CYAN}{length_ranges[word_length_setting][1]}{Fore.WHITE} letters)')
                    if word_length_setting.lower() == 'small' or word_length_setting.lower() == 'regular':
                        print(
                            f'Word Length: {Fore.GREEN}{word_length_setting}{Fore.WHITE} ({Fore.CYAN}{length_ranges[word_length_setting][0]}{Fore.WHITE}-{Fore.CYAN}{length_ranges[word_length_setting][1]}{Fore.WHITE} letters)')
                    if word_length_setting.lower() == 'longer':
                        print(
                            f'Word Length: {Fore.YELLOW}{word_length_setting}{Fore.WHITE} ({Fore.CYAN}{length_ranges[word_length_setting][0]}{Fore.WHITE}-{Fore.CYAN}{length_ranges[word_length_setting][1]}{Fore.WHITE} letters)')
                    if word_length_setting.lower() == 'greater' or word_length_setting.lower() == 'xtreme':
                        print(
                            f'Word Length: {Fore.RED}{word_length_setting}{Fore.WHITE} ({Fore.CYAN}{length_ranges[word_length_setting][0]}{Fore.WHITE}-{Fore.CYAN}{length_ranges[word_length_setting][1]}{Fore.WHITE} letters)')

                    # {Fore.GREEN}{word_length_setting}{Fore.WHITE}\n \n

                    print(f'Random word generated:\n')
                    random_word_pyfiglet = pyfiglet.figlet_format(
                        text=f'{random_word}', font='small')
                    print(f'{Fore.CYAN}{random_word_pyfiglet}{Fore.WHITE}')
                    print(f"'{random_word}'")
                    # {Fore.CYAN}{random_word_text}{Fore.WHITE}
                    sleep('...')

                elif tool_choice == 'i':
                    sleep('...')
                    img_prog_text = pyfiglet.figlet_format(
                        text='Img Prog', font="drpepper")
                    print(f'{img_prog_text}\n \n')
                    print(
                        f'The {Fore.CYAN}game difficulty{Fore.WHITE} is curently set to:\n')

                    if game_difficulty.lower() == 'very easy' or game_difficulty.lower() == 'easy':
                        print(f'{Fore.GREEN}{game_difficulty}{Fore.WHITE}')
                    if game_difficulty.lower() == 'medium' or game_difficulty.lower() == 'regular':
                        print(f'{Fore.BLUE}{game_difficulty}{Fore.WHITE}')
                    if game_difficulty.lower() == 'hard':
                        print(f'{Fore.YELLOW}{game_difficulty}{Fore.WHITE}')
                    if game_difficulty.lower() == 'xtra hard' or game_difficulty.lower() == 'impossible':
                        print(f'{Fore.RED}{game_difficulty}{Fore.WHITE}')

                    print(
                        f'\nThis setting allows for {Fore.GREEN}{difficulty_lives[game_difficulty.lower()]}{Fore.WHITE} wrong guesses.\nThe image progressions for this difficulty are as follows:\n \n')
                    print_starman_progression(game_difficulty)
                    print(f'{Fore.RED}MISSION FAILURE{Fore.WHITE}')
                    sleep('...')
                    break

                elif tool_choice == 'f':
                    sleep('...')
                    font_testing_text = pyfiglet.figlet_format(
                        text="Font Tester", font="charact1")
                    print(f'{font_testing_text}\n \n')
                    print(
                        f'Test how a word of your choice looks in various {Fore.CYAN}ASCII{Fore.WHITE} fonts')
                    print(f'{Fore.RED}*limit to 20 characters*{Fore.WHITE}\n \n')
                    while True:
                        text = input(
                            f'Please enter a {Fore.CYAN}search{Fore.WHITE} term: > ').strip()

                        if len(text) > 1 and len(text) < 21:
                            sleep('...')
                            test_fonts(text)
                            sleep('...')
                            break

                        elif len(text) < 1:
                            sleep('...')
                            invalid_text = pyfiglet.figlet_format(
                                text='IVALID', font='small')
                            print(f'{Fore.RED}{invalid_text}')
                            print(
                                f'Please enter a {Fore.CYAN}search{Fore.WHITE} term.')
                            sleep('...')

                        else:
                            sleep('...')
                            invalid_text = pyfiglet.figlet_format(
                                text='IVALID', font='small')
                            print(f'{Fore.RED}{invalid_text}')
                            print(
                                f'Please enter a valid {Fore.CYAN}search{Fore.WHITE} term.')
                            sleep('...')

                elif tool_choice == 'e':
                    sleep('...')
                    return_menu_text = pyfiglet.figlet_format(
                        text="BACK TO MENU", font='rectangles')
                    print(return_menu_text)
                    # print('//RETURNING TO MENU//')
                    sleep('...')
                    break

                else:
                    sleep('...')
                    invalid_text = pyfiglet.figlet_format(
                        text='IVALID', font='small')
                    print(f'{Fore.GREEN}{invalid_text}')
                    print("Please choose one of the options listed.")
                    sleep('...')

        else:
            # sleep('...')
            # invalid_text = pyfiglet.figlet_format(
            #     text='IVALID', font='small')
            # print(f'{Fore.RED}{invalid_text}')
            # print("Please choose one of the options listed.")
            # sleep('...')
            pass


if __name__ == "__main__":
    main_menu()
