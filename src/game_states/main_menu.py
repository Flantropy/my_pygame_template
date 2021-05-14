from box import Box
from game_states.game_state import GameState
from ultracolors import *
import pygame
from constants import CLOSE_GAME, DISPLAY_WIDTH


class MainMenu(GameState):
    def __init__(self):
        super(MainMenu, self).__init__()
        self.box = Box(VIOLET_BLUE)
        self.gfx.layer_0.add(self.box)
    
    def update(self):
        super().update()
        self.box.rect.move_ip(4, 0)
        if self.box.rect.x > DISPLAY_WIDTH - 100:
            pygame.event.post(pygame.event.Event(CLOSE_GAME))
