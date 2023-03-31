import pygame
from game_data import levels

class Narrator(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.sprites = []
        self.current_sprite = 0
        self.sprites.append(pygame.image.load('../animations/cat/1_Gato.png'))
        self.sprites.append(pygame.image.load('../animations/cat/2_Gato.png'))
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]

    def animate(self):
        self.current_sprite += 0.05
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]

    def update(self):    
        self.animate()

class Text:
    def __init__(self,current_level,surface,create_level):
        self.create_level = create_level
        self.display_surface = surface
        self.current_level = current_level
        level_data = levels[self.current_level]
        self.text = level_data['level_text']
        self.status = 'text'
        self.font = pygame.font.Font(None,40)
        self.narrator_sprites = pygame.sprite.Group()
        self.narrator = Narrator(750,300)
        self.narrator_sprites.add(self.narrator)

    def display_text(self,surface, text, pos, font, color):
        self.text = text
        collection = [word.split(' ') for word in self.text.splitlines()]
        space = font.size(' ')[0]
        x,y = pos
        for lines in collection:
            for words in lines:
                word_surface = font.render(words, True, color)
                word_width , word_height = word_surface.get_size()
                if x + word_width >= 1000:
                    x = pos[0]
                    y += word_height
                surface.blit(word_surface, (x,y))
                x += word_width + space
            x = pos[0]
            y += word_height
        

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN] and self.status == 'text':
            self.create_level(self.current_level)

    def run(self):
        self.get_input()
        self.display_surface.fill((0,0,0))
        self.display_text(self.display_surface,self.text,(200,20),self.font,'White')
        self.narrator_sprites.draw(self.display_surface)
        self.narrator.update()


