import pygame

class UI:
    def __init__(self,surface):

        self.display_surface = surface

        self.health_bar = pygame.image.load('../animations/health_bar.png').convert_alpha()
        self.health_bar_topleft = (54,39)
        self.bar_max_width = 152
        self.bar_height = 4


    def show_health(self,current,full):
        self.display_surface.blit(self.health_bar,(20,10))
        current_health_ratio = current / full
        current_bar_width = self.bar_max_width * current_health_ratio
        health_bar_rect = pygame.Rect(self.health_bar_topleft, (current_bar_width,self.bar_height))
        pygame.draw.rect(self.display_surface, '#dc4949',health_bar_rect)

class Screen_Text:
    def __init__(self,surface):
        self.display_surface = surface
        text = "Utilize -> para selecionar o próximo nível"
        self.font = pygame.font.Font(None,20)
        self.text_surf = self.font.render(text,True,'White')
        self.text_rect = self.text_surf.get_rect(center = (200,500))
        text1 = "Utilize <- para voltar ao nível anterior"
        self.text_surf1 = self.font.render(text1,True,'White')
        self.text_rect1 = self.text_surf.get_rect(center = (200,550))
        text2= "Aperte espaço para selecionar o nível"
        self.text_surf2 = self.font.render(text2,True,'White')
        self.text_rect2 = self.text_surf.get_rect(center = (200,600))

    def show_text(self):
        self.display_surface.blit(self.text_surf, self.text_rect)
        self.display_surface.blit(self.text_surf1, self.text_rect1)
        self.display_surface.blit(self.text_surf2, self.text_rect2)