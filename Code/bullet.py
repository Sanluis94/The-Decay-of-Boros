import pygame
from config import screen_width,tile_size
from tiles import Tile

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y, facing):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 13
        self.image = pygame.Surface((20,5))
        self.rect = self.image.get_rect()
        self.facing = facing
        if facing:
            self.rect.center = (x + 63, y + 55)
            self.direction = 1
        if not facing:
            self.rect.center = (x - 10, y + 55)
            self.direction = - 1

    def update(self):
        self.rect.x += (self.direction * self.speed)

        if self.rect.right < 0 or self.rect.left > screen_width:
            self.kill() 

     

