from PIL import Image, ImageSequence
import pygame

def loadGIF(filename):
    pilImage = Image.open(filename)
    frames = []
    for frame in ImageSequence.Iterator(pilImage):
        frame = frame.convert('RGBA')
        pygameImage = pygame.image.fromstring(
            frame.tobytes(), frame.size, frame.mode).convert_alpha()
        frames.append(pygameImage)
    return frames

class Evil_die(pygame.sprite.Sprite):
    def __init__(self , pos):
        super().__init__()
        self.gif_images = loadGIF('try_again/giphy.gif')

        self.images = self.gif_images
        self.image = self.images[0]
        # print(type(self.image))
        self.rect = self.image.get_rect(topleft = pos)
        self.image_index = 0

        # self.image = pygame.image.load(r'try_again/33HS.gif')
        # self.image = pygame.transform.scale(self.image, (screen_tile, screen_tile))
        # # self.image.fill("purple")
        # self.rect = self.image.get_rect(topleft = pos)
    


    def update(self):
        self.image_index += 1
        if self.image_index >= len(self.images):
            self.image_index = 0

        self.image = self.images[self.image_index]