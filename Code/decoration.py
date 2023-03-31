import pygame
from config import screen_width, screen_height

class Sky:
    def __init__(self):
        self.Sky = pygame.image.load('../levels/Sky.png')

        self.Sky = pygame.transform.scale(self.Sky,(screen_width,screen_height))

    def draw(self,surface):
        surface.blit(self.Sky,(0,0))

class Overworld_BG:
    def __init__(self):
        self.overworld_background = pygame.image.load('../levels/overworld_background.png')

        self.overworld_background = pygame.transform.scale(self.overworld_background,(screen_width,screen_height))

    def draw(self,surface):
        surface.blit(self.overworld_background,(0,0))         