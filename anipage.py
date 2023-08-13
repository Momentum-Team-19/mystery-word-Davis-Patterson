from random import randint
from asciimatics.screen import Screen
import time


def demo(screen):
    animation_start_time = time.time()
    animation_duration = 4

    while time.time() - animation_start_time < animation_duration:
        screen.print_at('Victory!',
                        randint(0, screen.width), randint(0, screen.height),
                        colour=randint(0, screen.colours - 1),
                        bg=randint(0, screen.colours - 1))
        ev = screen.get_key()
        if ev in (ord('Q'), ord('q')):
            return
        screen.refresh()


def start_screen():
    Screen.wrapper(demo)
