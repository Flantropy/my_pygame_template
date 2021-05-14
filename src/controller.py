import pygame

from constants import FPS, CLOSE_GAME, LOAD_MENU
from fsm import FSM
from game_states.load_screen import LoadScreen
from game_states.main_menu import MainMenu


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
            # TODO
            """
            Try to check here only 'state-changing' events
            and left all 'user I/O' events for check inside a Game Scene
            """
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == CLOSE_GAME:
                    self.controller.close()
                if event.type == LOAD_MENU:
                    self.controller.load()
            
            self.controller.model.current_scene.update()
            
            self.display.fill((0, 0, 0))
            self.controller.model.current_scene.render(self.display)
            pygame.display.update()
