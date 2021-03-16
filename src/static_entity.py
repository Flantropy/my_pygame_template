import pygame
import constants as c


class StaticEntity(pygame.sprite.Sprite):
	def __init__(self, image=pygame.Surface(c.MEDIUM_TILE_SIZE)):
		super(StaticEntity, self).__init__()
		self.image = image
		self.rect = self.image.get_rect()
		self.pos_x = 0.0
		self.pos_y = 0.0
		self.vel_x = 0.0
		self.vel_y = 0.0
	
	def _update(self, *args, **kwargs):
		self.update_pos()
	
	def update_pos(self):
		self.pos_x += self.vel_x
		self.rect.x = int(self.pos_x)
		self.pos_y += self.vel_y
		self.rect.y = int(self.pos_y)
