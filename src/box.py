from pygame import Surface
from pygame.sprite import Sprite


class Box(Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = Surface((100, 100))
        self.rect = self.image.get_rect()
        self.color = color
        self.image.fill(self.color)
