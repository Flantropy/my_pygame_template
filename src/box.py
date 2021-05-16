from pygame import Surface
from pygame.sprite import Sprite


class Box(Sprite):
    def __init__(self, color, x=0, y=0):
        super().__init__()
        self.image = Surface((50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.color = color
        self.image.fill(self.color)
