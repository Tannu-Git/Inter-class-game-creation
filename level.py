
import pygame
from scipy.fftpack import shift
from animations import Evil_die
from coin import Coin
from evil import  Evil_Banshee, Evil_Dragon, Winner_logo
from invisible_box import Inivsible
from plat import Tile
from setup import screen_tile , screen_width , screen_height
from player import Player

class Level():
    def __init__(self , level_data , surface):
        self.display_surface = surface
        self.level_dataa = level_data
        self.setup_level(level_data)
        self.shift = 0
        self.score = 0
        self.lives = 3
        self.score = 0

    def setup_level(self , level_data):
        self.tiles = pygame.sprite.Group()
        self.invi = pygame.sprite.Group()
        self.coin = pygame.sprite.Group()
        self.players = pygame.sprite.GroupSingle()
        self.winnner = pygame.sprite.GroupSingle()
        self.evils = pygame.sprite.Group()
        for row_index,row in enumerate(level_data):
            for col_index,col_data in enumerate(row):
                if col_data == "d":
                    x = col_index * screen_tile
                    y = (row_index * screen_tile)
                    invisi_box = Inivsible((x,y))
                    self.invi.add(invisi_box)
                if col_data.isnumeric():
                    x = col_index * screen_tile
                    y = row_index * screen_tile
                    tile = Tile((x,y) , screen_tile, f'try_again/tile_try/new_tile_coding/{col_data}.png')
                    self.tiles.add(tile)
                if col_data == "x":
                    x = col_index * screen_tile
                    y = row_index * screen_tile
                    tile = Tile((x,y) , screen_tile , 'try_again/33HS.gif')
                    self.tiles.add(tile)
                if col_data == "c":
                    x = col_index * screen_tile
                    y = (row_index * screen_tile)
                    coins = Coin((x,y))
                    self.coin.add(coins)
                elif col_data == "y":
                    x = col_index * screen_tile
                    y = row_index * screen_tile
                    player = Player((x,y))
                    self.players.add(player)
                if col_data == "e":
                    x = col_index * screen_tile
                    y = (row_index * screen_tile) +1
                    evils = Evil_Banshee((x,y))
                    self.evils.add(evils)
                if col_data == "w":
                    x = col_index * screen_tile
                    y = (row_index * screen_tile)
                    winner = Winner_logo((x,y))
                    self.winnner.add(winner)
                if col_data == "dr":
                    x = col_index * screen_tile
                    y = (row_index * screen_tile) +1
                    evils = Evil_Dragon((x,y))
                    self.evils.add(evils)
                
                
    def scroll_on_x(self):
        player = self.players.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        if player_x < screen_width/5 and direction_x < 0:
            self.shift = 6
            player.speed = 0
        elif player_x > (screen_width- (screen_width /5)) and direction_x > 0:
            self.shift = -6
            player.speed = 0
        else:
            self.shift = 0
            player.speed = 6

    def Horizontal_collision(self):
        player = self.players.sprite
        player.rect.x += player.direction.x * player.speed
        for i in self.tiles.sprites():
            if i.rect.colliderect(player.rect):
                if player.direction.x < 0 :
                    player.rect.left = i.rect.right 
                elif player.direction.x >0:
                    player.rect.right = i.rect.left

    def Vertical_collision(self):
        player = self.players.sprite
        player.Gravity()
        for i in self.tiles.sprites():
            if i.rect.colliderect(player.rect):
                if player.direction.y < 0 :
                    player.rect.top = i.rect.bottom
                    player.direction.y = 0
                elif player.direction.y >0:
                    player.rect.bottom = i.rect.top 
                    player.direction.y = 0

    def Evil_collisoin(self):
        evils = self.evils.sprites()
        for i in evils:
            if i.rect.colliderect(self.players.sprite.rect):
                if self.players.sprite.direction.y > 0:
                    i.kill()
                else:
                    self.out_reset()
    def evil_collide_check(self):
        evilss= self.evils.sprites()
        for i in evilss:
            for h in self.invi.sprites():
                if i.rect.colliderect(h.rect):
                    i.image = pygame.transform.flip(i.image , True,False)
                    if i.evil_right == True:
                        i.evil_right = False
                    elif i.evil_right == False:
                        i.evil_right = True

    def level_complete(self):
        win = self.winnner.sprite
        if win.rect.colliderect(self.players.sprite.rect):
            print('win')

    def evil_movement(self):
        evilss= self.evils.sprites()
        for i in evilss:
            for o in self.tiles.sprites():
                if i.rect.colliderect(o.rect):
                    i.rect.centerx += i.direction_x
                   
    def coin_collide(self):
        coinss = self.coin.sprites()
        players = self.players.sprite
        for i in coinss:
            if players.rect.colliderect(i.rect):
                self.score += 1
                i.kill()
        
        

    def fall(self):
        if self.players.sprite.rect.y > screen_height :
            self.out_reset()
    
    def out_reset(self):
        self.tiles = pygame.sprite.Group()
        self.players = pygame.sprite.GroupSingle()
        self.evils = pygame.sprite.Group()
        self.setup_level(self.level_dataa)
        self.score = 0
        if self.lives >0:
            self.lives -=1
        else:
            print("Main menu")



    def run(self):
        self.tiles.update(self.shift)
        self.tiles.draw(self.display_surface)
        self.scroll_on_x()
        self.players.update()
        self.Vertical_collision()
        self.Horizontal_collision()
        self.players.draw(self.display_surface)
        self.coin.draw(self.display_surface)
        self.coin.update(self.shift)
        self.coin_collide()
        self.winnner.draw(self.display_surface)
        self.winnner.update(self.shift)
        self.evil_movement()
        self.evil_collide_check()
        self.evils.draw(self.display_surface)
        self.evils.update(self.shift)
        self.invi.draw(self.display_surface)
        self.invi.update(self.shift)
        self.Evil_collisoin()
        self.fall()
        self.level_complete()


