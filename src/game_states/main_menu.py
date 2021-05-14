from box import Box
from constants import DISPLAY_WIDTH
from game_states.game_state import GameState
from ultracolors import *


class MainMenu(GameState):
    def __init__(self, fsm):
        super(MainMenu, self).__init__(fsm=fsm)
        self.box = Box(VIOLET_BLUE)
        self.gfx.layer_0.add(self.box)
    
    def update(self):
        super().update()
        self.box.rect.move_ip(4, 0)
        if self.box.rect.x > DISPLAY_WIDTH - 100:
            self.fsm.close()
