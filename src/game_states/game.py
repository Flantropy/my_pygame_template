import pygame

from box import Box
from constants import PAUSE
from game_states import GameState
from ultracolors import *


class Game(GameState):
    def __init__(self):
        super(Game, self).__init__()
        self.pause_box = Box(BLUE, x=430)
        self.gfx.layer_0.add(self.pause_box)
    
    def update(self):
        super().update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.pause_box.rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.event.post(pygame.event.Event(PAUSE))
