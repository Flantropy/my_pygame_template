import pygame

from box import Box
from constants import DISPLAY_HEIGHT, LOAD_MENU
from game_states.game_state import GameState
from ultracolors import *


class LoadScreen(GameState):
    def __init__(self):
        super(LoadScreen, self).__init__()
        self.box = Box(GREEN_1)
        self.gfx.layer_0.add(self.box)
    
    def update(self):
        super().update()
        self.box.rect.move_ip(0, 2)
        if self.box.rect.y > DISPLAY_HEIGHT - 100:
            pygame.event.post(pygame.event.Event(LOAD_MENU))
