import pygame
from sys import exit
from level import Level
from setup import *

# w = int(input("Width: "))
# h = int(input("Height: "))
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
level = Level(level_data=l_map , surface=screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


        #game code
    screen.fill('black')
    level.run()

    pygame.display.update()
    clock.tick(60)