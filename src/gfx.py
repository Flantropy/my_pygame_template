import pygame


class GFX:
    def __init__(self):
        self.layer_0 = pygame.sprite.Group()  # BG 2
        self.layer_1 = pygame.sprite.Group()  # BG 1
        self.layer_2 = pygame.sprite.Group()  # Platforms / Tiles
        self.layer_3 = pygame.sprite.Group()  # Enemies
        self.layer_4 = pygame.sprite.Group()  # Player
        self.layer_5 = pygame.sprite.Group()  # Projectiles / Items
        self.layer_6 = pygame.sprite.Group()  # FG
        self.layer_7 = pygame.sprite.Group()  # HUD
        self.layers = [
            self.layer_0,
            self.layer_1,
            self.layer_2,
            self.layer_3,
            self.layer_4,
            self.layer_5,
            self.layer_6,
            self.layer_7]
    
    def update(self):
        for layer in self.layers:
            layer.update()
    
    def render(self, display):
        for layer in self.layers:
            layer.draw(display)
