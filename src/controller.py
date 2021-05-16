import pygame

from constants import (
    FPS, CLOSE_GAME, LOAD_MENU, PLAY, PAUSE,
    RESUME, QUIT_TO_MENU, STATE_CHANGING_EVENTS
)
from fsm import FSM
from game_states import LoadScreen, MainMenu
from ultracolors import BLACK


class Model(object):
    scenes = dict(loadscreen=LoadScreen, main_menu=MainMenu)
    
    def __init__(self, state):
        self.state = state
        self.current_scene = self.scenes[self.state]()


class Controller:
    def __init__(self, display, clock):
        self.display = display
        self.clock = clock
        self.model = Model(state=FSM.loadscreen.identifier)
        self.controller = FSM(self.model)
        
    def run_game(self):
        while True:
            self.clock.tick(FPS)
            for event in pygame.event.get(STATE_CHANGING_EVENTS):
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == CLOSE_GAME:
                    self.controller.close()
                if event.type == LOAD_MENU:
                    self.controller.load()
                if event.type == PLAY:
                    self.controller.play()
                if event.type == PAUSE:
                    self.controller.pause()
                if event.type == QUIT_TO_MENU:
                    self.controller.quit()
                if event.type == RESUME:
                    self.controller.resume()
                    
            self.controller.model.current_scene.update()
            
            self.display.fill(BLACK)
            self.controller.model.current_scene.render(self.display)
            pygame.display.update()
