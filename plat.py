import pygame
class Tile(pygame.sprite.Sprite):
    def __init__(self , pos, size,image):
        super().__init__()
        # this creates a rectangular surface over an old surface with some size and position  
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image , (size , size))
        # print(pos)
        self.rect = self.image.get_rect(topleft = pos)
    
    def update(self , shift):
        # addind value at x axis to move all the tiles
        self.rect.x += shift
        # print(self.rect.x) 
