from box import Box
from constants import DISPLAY_HEIGHT
from game_states.game_state import GameState
from ultracolors import *


class LoadScreen(GameState):
    def __init__(self, fsm):
        super(LoadScreen, self).__init__(fsm=fsm)
        self.box = Box(GREEN_1)
        self.gfx.layer_0.add(self.box)
    
    def update(self):
        super().update()
        self.box.rect.move_ip(0, 2)
        if self.box.rect.y > DISPLAY_HEIGHT - 100:
            self.fsm.load()
