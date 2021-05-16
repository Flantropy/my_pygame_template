import pygame

from box import Box
from constants import QUIT_TO_MENU, RESUME
from game_states import GameState
from ultracolors import *


class Pause(GameState):
    def __init__(self):
        super(Pause, self).__init__()
        self.quit_box = Box(RED)
        self.resume_box = Box(WHITE, x=430)
        self.gfx.layer_0.add(self.quit_box, self.resume_box)
    
    def update(self):
        super().update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pos()
                if self.quit_box.rect.collidepoint(click):
                    pygame.event.post(pygame.event.Event(QUIT_TO_MENU))
                if self.resume_box.rect.collidepoint(click):
                    pygame.event.post(pygame.event.Event(RESUME))
