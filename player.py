import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image  = pygame.image.load(r'try_again/Chara - BlueIdle00017.png')
        self.image = pygame.transform.scale(self.image , (64 , 64))
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 6
        self.gravity = 0.6
        self.jump_height  = -10

    def move_player(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def Gravity(self):
            self.direction.y += 1
            self.rect.y += self.direction.y
    def Jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction.y = self.jump_height
            self.rect.y += self.direction.y

    def update(self):
        self.move_player()
        self.Jump()
