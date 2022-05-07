import pygame
from setup import screen_tile
class Inivsible(pygame.sprite.Sprite):
    def __init__(self , pos):
        super().__init__()
        self.image = pygame.Surface((screen_tile,screen_tile))
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect(topleft = pos)
        self.direction_x = 0 
        self.evil_right = True

    
    def update(self , shift):
        self.rect.x += shift
