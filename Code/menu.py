import pygame

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -300

    def draw_cursor(self):
        self.game.draw_text('*', 37, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Jogar"
        self.startx, self.starty = self.mid_w, self.mid_h + 8
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 50
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 90
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('The Decay of Boros', 70, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 90)
            self.game.draw_text("Jogar", 30, self.startx, self.starty)
            self.game.draw_text("Opcoes", 30, self.optionsx, self.optionsy)
            self.game.draw_text("Creditos", 30,self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()

 
    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Jogar':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Opcoes'
            elif self.state == 'Opcoes':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Creditos'
            elif self.state == 'Creditos':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Jogar'
        elif self.game.UP_KEY:
            if self.state == 'Jogar':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Creditos'
            elif self.state == 'Opcoes':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Jogar'
            elif self.state == 'Creditos':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Opcoes'
            
    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Jogar':
                self.game.playing = True
            elif self.state == 'Opcoes':
                self.game.curr_menu = self.game.options
            elif self.state == 'Creditos':
                self.game.curr_menu = self.game.credits    
            self.run_display = False

class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 40
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 90
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Opcoes', 60, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text("Volume", 20, self.volx, self.voly)
            self.game.draw_text("Controles", 20, self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controles'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == 'Controles':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        elif self.game.START_KEY:
            # TO-DO: Create a Volume Menu and a Controls Menu
            pass

class CreditsMenu (Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
    
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Creditos', 50, self.game.DISPLAY_W /2, self.game.DISPLAY_H /2 - 190)
            self.game.draw_text('Criado por', 30, self.game.DISPLAY_W /2, self.game.DISPLAY_H /2 - 105)
            self.game.draw_text('Murilo Goes ', 15, self.game.DISPLAY_W /2, self.game.DISPLAY_H /2 + 10 )
            self.game.draw_text('Luis Antonio de Albuquerque ', 15, self.game.DISPLAY_W /2, self.game.DISPLAY_H /2 - 50 )
            self.game.draw_text('Luis Filipe Giglio ', 15, self.game.DISPLAY_W /2, self.game.DISPLAY_H /2 - 20 )
            self.game.draw_text('Pedro Ludovico ', 15, self.game.DISPLAY_W /2, self.game.DISPLAY_H /2 + 40 )
            self.game.draw_text('Vinicius Fernandes ', 15, self.game.DISPLAY_W /2, self.game.DISPLAY_H /2 + 70 )
            
            
            self.blit_screen()