import pygame
from static_entity import StaticEntity
import ultracolors as color
import constants as c
# from animation import AnimationGroup
# from entity_state import EntityStateGroup()


class DynamicEntity(StaticEntity):
	def __init__(self, image=pygame.Surface(c.MEDIUM_TILE_SIZE)):
		super(DynamicEntity, self).__init__(image)
		self.color = color.BLUE
		self.image.fill(self.color)
		# self.animation = AnimationGroup()
		# self.state = EntityStateGroup()
		
	def update(self):
		self.update_pos()
		self.update_state()
		self.update_animation()
	
	def update_state(self):
		pass
	
	def update_animation(self):
		pass
