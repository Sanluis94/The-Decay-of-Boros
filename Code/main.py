#Acessar cd Projeto-integrador\Code paraa rodar o programa

import pygame, sys
from config import *
from level import Level
from game_data import levels
from overworld import Overworld
from UI import UI
from menu import *
from text import *
from UI import Screen_Text

pygame.init() #Necessário para inicializar o pygame
screen = pygame.display.set_mode((screen_width,screen_height)) #Permite a tela aparecer
pygame.display.set_caption("The Decay of Boros")
clock = pygame.time.Clock() #Inicializa a contagem dos quadros

class Game:
    def __init__(self):
        self.max_level = 3
        self.max_health = 100
        self.cur_health = 100
        self.overworld = Overworld(3,self.max_level,screen,self.create_level,self.create_text,self.display_text)
        self.status = 'overworld'

        self.ui = UI(screen)
        self.text_over = Screen_Text(screen)

    def create_level(self,current_level):
        self.level = Level(current_level,screen,self.create_overworld,self.change_health)
        self.status = 'level'

    def create_overworld(self,current_level,new_max_level):
        if new_max_level > self.max_level:
            self.max_level = new_max_level
        self.overworld = Overworld(current_level,self.max_level,screen,self.create_level,self.create_text,self.display_text)
        self.status = 'overworld'

    def create_text(self,current_level):
        self.text = Text(current_level,screen,self.create_level)
        self.status = 'text'

    def display_text(self):
        self.display = Text(self.display_surface)

    def change_health(self,amount):
        self.cur_health += amount

    def check_game_over(self):
        if self.cur_health <= 0:
            self.cur_health = 100
            self.max_level = 0
            self.overworld = Overworld(0,self.max_level,screen,self.create_level,self.create_text,self.display_text)
            self.status = 'overworld'

    def run(self):
        if self.status == 'overworld':
            self.overworld.run()
            self.text_over.show_text()
        elif self.status == 'text':
            self.text.run()
        else:
            self.level.run()
            self.ui.show_health(self.cur_health,self.max_health)
            self.check_game_over()

game = Game()

class menu():
    def __init__(self):
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = screen_width, screen_height
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.font_name = '8-BIT WONDER.TTF'
        #self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.BACK_KEY:
                self.playing= False
            self.display.fill(self.BLACK)
            game.run() #A função .run() permite a execução de outras funções, neste caso a função Level
    
            pygame.display.update()#Faz com que a tela apareça
            clock.tick(60) #Taxa de fps (quadros por segundo)
            self.reset_keys()



    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_ESCAPE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
            self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y ):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)

m = menu()

while m.running:# inicializa o processo do jogo e mantém ele rodando

    m.curr_menu.display_menu()
    m.game_loop()

