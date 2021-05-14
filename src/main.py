import pygame
from constants import DISPLAY_SIZE
from controller import Controller


def main():
    display = pygame.display.set_mode(DISPLAY_SIZE)
    clock = pygame.time.Clock()
    controller = Controller(display, clock)
    controller.run_game()


if __name__ == '__main__':
    main()
