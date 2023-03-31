from random import randint
import pygame
from tiles import AnimatedTile

class Enemy(AnimatedTile):
    def __init__(self,size,x,y):
        super().__init__(size,x,y,'../levels/ghost')
        self.rect.y -= 25
        self.speed = randint(2,4)

    def move(self):
        self.rect.x += self.speed

    def reverse_image(self):
        if self.speed < 0:
            self.image = pygame.transform.flip(self.image,True,False)

    def reverse(self):
        self.speed *= -1
    
    def update(self,shift):
        self.rect.x += shift
        self.animate()
        self.move()
        self.reverse_image()    

class Dragon(AnimatedTile):
    def __init__(self,size,x,y):
        super().__init__(size,x,y,'../levels/Dragon')
        self.rect.y -= 25
        self.speed = 3

    def move(self):
        self.rect.x += self.speed

    def reverse_image(self):
        if self.speed < 0:
            self.image = pygame.transform.flip(self.image,True,False)

    def reverse(self):
        self.speed *= -1
    
    def update(self,shift):
        self.rect.x += shift
        self.animate()
        self.move()
        self.reverse_image()   