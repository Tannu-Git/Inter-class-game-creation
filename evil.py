import pygame
from setup import screen_tile
class Evil_Banshee(pygame.sprite.Sprite):
    def __init__(self , pos):
        super().__init__()
        self.image = pygame.image.load(f'try_again/Banshee.png')
        self.image = pygame.transform.scale(self.image , (screen_tile,screen_tile))
        self.rect = self.image.get_rect(topleft = pos)
        self.image = pygame.transform.flip(self.image , True,False)
        self.direction_x = 0 
        self.evil_right = True
    
    def move(self):
        if self.evil_right == True:
            self.direction_x = 1
        else:
            self.direction_x = -1
    
    def update(self , shift):
        self.rect.x += shift
        self.move()

class Evil_Dragon(pygame.sprite.Sprite):
    def __init__(self , pos):
        super().__init__()
        self.image = pygame.image.load(f'try_again/sunny-dragon-fly.gif')
        self.image = pygame.transform.scale(self.image , (screen_tile,screen_tile))
        self.rect = self.image.get_rect(topleft = pos)
        self.image = pygame.transform.flip(self.image , True,False)
        self.direction_x = 0 
        self.evil_right = True
    
    def move(self):
        if self.evil_right == True:
            self.direction_x = 1
        else:
            self.direction_x = -1
    
    def update(self , shift):
        self.rect.x += shift
        self.move()

class Winner_logo(pygame.sprite.Sprite):
    def __init__(self , pos):
        super().__init__()
        self.image = pygame.image.load(f'try_again/wizard.png')
        self.image = pygame.transform.scale(self.image , (screen_tile,screen_tile))
        self.rect = self.image.get_rect(topleft = pos)

    
    def update(self , shift):
        self.rect.x += shift
