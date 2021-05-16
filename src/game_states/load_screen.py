import pygame

from box import Box
from constants import LOAD_MENU
from game_states.game_state import GameState
from ultracolors import YELLOW


class LoadScreen(GameState):
    def __init__(self):
        super(LoadScreen, self).__init__()
        self.box = Box(YELLOW, x=430, y=220)
        self.gfx.layer_0.add(self.box)
    
    def update(self):
        super().update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.box.rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.event.post(pygame.event.Event(LOAD_MENU))
