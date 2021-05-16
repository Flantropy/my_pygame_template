import pygame

from box import Box
from constants import CLOSE_GAME, PLAY
from game_states import GameState
from ultracolors import *


class MainMenu(GameState):
    def __init__(self):
        super(MainMenu, self).__init__()
        self.close_box = Box(VIOLET_BLUE)
        self.play_box = Box(LAWN_GREEN, x=210, y=120)
        self.gfx.layer_0.add(self.close_box, self.play_box)
    
    def update(self):
        super().update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pos()
                if self.close_box.rect.collidepoint(click):
                    pygame.event.post(pygame.event.Event(CLOSE_GAME))
                if self.play_box.rect.collidepoint(click):
                    pygame.event.post(pygame.event.Event(PLAY))
