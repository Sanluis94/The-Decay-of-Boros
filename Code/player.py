import pygame
from support import import_folder
from math import sin
from config import screen_width,tile_size
from bullet import Bullet
from enemy import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,surface,change_health):
        super().__init__() #Inicia os processos das funções
        self.import_character_assets() #importa as imagens da pasta com as imagens do personagem
        self.display_surface = surface
        self.frame_index = 0 #Índice do frame que será mostrado
        self.animation_speed = 0.15 #Velocidade com que são trocados os frames
        self.image = self.animations['idle'][self.frame_index] #Frame padrão que é mostrado, alterado pela função get.status()
        self.rect = self.image.get_rect(topleft = pos) #Posição padrão do personagem

        self.direction = pygame.math.Vector2(0,0)
        self.speed = 6 #Velocidade do personagem
        self.gravity = 0.8 #Velocidade de queda
        self.jump_speed = -16 #velocidade de subida (pulo)

        #Reconhece os status da colisão personagem, validando com verdadeiro ou falso para qual colisão ocorre no momento
        self.status = 'idle' 
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
        self.shooting = False

        self.change_health = change_health
        self.invincible = False
        self.invincibility_duration = 400
        self.hurt_time = 0 

        self.bullets = pygame.sprite.Group()      
        self.shot =  False
        self.shoot_cooldown = 0
        self.boss_health = 8
        
    def import_character_assets(self):
        character_path = '../animations/' #Pasta onde se encontram as animações
        self.animations = {'idle': [], 'walk':[], 'jump':[],'fall':[], 'shoot':[]} #Listas onde as animações apresentadas são armazenadas

        for animation in self.animations.keys(): 
            full_path = character_path + animation #Diretório completo, que permite o correto direcionamento para as animações
            self.animations[animation] = import_folder(full_path) #Função que permite importar a pasta e indexar nas listas

    def animate(self): #Função que permite a animação do personagem
        animation = self.animations[self.status]   #Indexa os status para serem animados encontrados no dicionário animations

        #Pemite a troca dos frames 
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        
        #Transorma o index de string para inteiro para perimitir a a indexação e o uso da funçao .transform()
        image = animation[int(self.frame_index)]   
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image,True,False)
            self.image = flipped_image

        if self.invincible:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

        #Verificação das colisões

        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        if self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)

    def get_input(self): #Recebe os eventos do teclado
        keys = pygame.key.get_pressed() #Verifica quando as teclas são pressionadas
        self.bullet = Bullet(self.rect.x, self.rect.y, self.facing_right)       
        
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]: #Permite a tecla d e a seta para direita movimentarem o personagem para am direita
            self.direction.x = 1
            self.facing_right = True
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]: #Premite a tecla a e a seta para a direita movimentarem o personagem para a direita
            self.direction.x = -1
            self.facing_right = False
        else: #Caso não ocorra input de direção horizontal, o personagem permanece parado
            self.direction.x = 0

        if (keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]) and self.on_ground: #Permite o espaço, a tecla w e a set para cima fazerem o personagem pular
            self.jump()
        
        if (keys[pygame.K_LSHIFT] and keys[pygame.K_d] or keys[pygame.K_LSHIFT] and keys[pygame.K_RIGHT]) and self.rect.x <= screen_width - (screen_width / 4):
            self.speed = 10
            self.gravity = 1
            self.animation_speed = 0.5
        elif (keys[pygame.K_LSHIFT] and keys[pygame.K_LEFT] or keys[pygame.K_LSHIFT] and keys[pygame.K_a]) and self.rect.x >= screen_width / 4:
            self.speed = 10
            self.gravity = 1
            self.animation_speed = 0.5

        if keys[pygame.K_k]:
            if self.shoot_cooldown == 0:
                self.shoot_cooldown = 20
                self.shot = True
                self.bullets.add(self.bullet)
                self.shooting = True
                self.animation_speed = 0.5
        else:
            self.shooting = False
            self.shot = False



    def get_status(self): #Função que procura as informações do status de movimento do personagem
        if self.shooting:
            self.status = 'shoot'

        #Movimento vertical
        if not self.shooting:
            if self.direction.y < 0: #Reconhece o movimento vertical e executa a animação do pulo
                self.status = 'jump' 
            elif self.direction.y > 1: #Reconhece o movimento vertical e executa a animação de queda
                self.status = 'fall'
            #Movimento horizontal
            else:
                if self.direction.x != 0: #Verifica se existe movimento horizontal e retorna a animação de andar
                    self.status = 'walk'

                else: #Caso nenhuma das possibilidades acima sejam verdadeiras, o personagem permanece imóvel
                    self.status = 'idle'

    def apply_gravity(self): #Função que aplica a funcionalidade da gravidade
        self.direction.y += self.gravity
        self.rect.y += self.direction.y 

    def jump(self): #Função que aplica a funcionalidade do pulo
        self.direction.y = self.jump_speed
        
    def get_damage(self):
        if not self.invincible:
            self.change_health(-10)
            self.invincible = True
            self.hurt_time = pygame.time.get_ticks()

    def invincibility_timer(self):
        if self.invincible:
            current_time = pygame.time.get_ticks()
            if current_time - self.hurt_time >= self.invincibility_duration:
                self.invincible = False

    def wave_value(self):
        value = sin(pygame.time.get_ticks())
        if value >= 0: return 255
        else: return 0

    def cooldown(self):
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    def bullet_ground(self,ground):
        collide = pygame.sprite.groupcollide(ground,self.bullets,False,True)

    def bullet_enemy(self,enemy):
        collide = pygame.sprite.groupcollide(enemy,self.bullets,True,True)
        
    def bullet_boss(self,boss):
        if self.boss_health <= 0:
            check = True
        else:
            check = False

        collide = pygame.sprite.groupcollide(boss,self.bullets,check,True)

        if collide:
            self.boss_health -= 1
            print(self.boss_health)

    def update(self,ground,enemy,boss): #.Update() atualiza  a tela, aplicando as demais funções no aplicativo/display
        self.get_input()
        self.get_status()
        self.animate()
        self.invincibility_timer()
        self.wave_value()
        self.bullets.draw(self.display_surface)
        self.bullets.update()
        self.cooldown()
        self.bullet_ground(ground)
        self.bullet_enemy(enemy)
        self.bullet_boss(boss)

