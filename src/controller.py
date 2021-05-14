import pygame

import constants as c
from event_handler import EventHandler
from fsm import FSM
from game_states.load_screen import LoadScreen
from game_states.main_menu import MainMenu


class Controller:
    states = dict(loadscreen=LoadScreen, main_menu=MainMenu)
    
    def __init__(self, display, clock):
        self.display = display
        self.clock = clock
        self.fsm = FSM()
        self.event_handler = EventHandler()
        self.current_state = LoadScreen(fsm=self.fsm)
    
    def run_game(self):
        while True:
            # Tick Clock
            self.clock.tick(c.FPS)
            # Handle Events
            self.event_handler.handle_events()
            
            # Update State
            self.current_state.update()
            
            # Render State
            self.display.fill((0, 0, 0))
            self.current_state.render(self.display)
            pygame.display.update()
            self.update_fsm()
    
    def update_fsm(self):
        if self.current_state.__class__ != self.states[self.fsm.current_state.identifier]:
            self.current_state = self.states[self.fsm.current_state.identifier](self.fsm)
