from gfx import GFX


class GameState:
	def __init__(self, fsm):
		self.gfx = GFX()
		self.fsm = fsm
	
	def update(self):
		self.gfx.update()
	
	def render(self, display):
		self.gfx.render(display)
