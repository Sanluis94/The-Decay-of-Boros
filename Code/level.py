import pygame
from support import import_csv_layout,import_cut_graphic
from config import tile_size, screen_width, screen_height
from tiles import Tile, StaticTile, Torch, AnimatedTile
from enemy import *
from decoration import Sky
from player import * 
from game_data import levels

class Level:
    def __init__(self,current_level,surface,create_overworld,change_health):
        self.display_surface = surface     
        self.world_shift = 0
        self.current_x = None

        self.create_overworld = create_overworld
        self.current_level = current_level
        level_data = levels[self.current_level]
        self.new_max_level = level_data['unlock']

        player_layout = import_csv_layout(level_data['player'])
        self.player = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()
        self.player_setup(player_layout,change_health)

        terrain_layout = import_csv_layout(level_data['terrain'])
        self.terrain_sprites = self.create_tile_group(terrain_layout,'terrain')

        torch_layout = import_csv_layout(level_data['torch'])
        self.torch_sprites = self.create_tile_group(torch_layout,'torch')

        enemies_layout = import_csv_layout(level_data['enemies'])
        self.enemies_sprites = self.create_tile_group(enemies_layout,'enemies')

        constraint_layout = import_csv_layout(level_data['constraints'])
        self.constraint_sprites = self.create_tile_group(constraint_layout,'constraints')

        dragon_layout = import_csv_layout(level_data['boss'])
        self.dragon_sprites = self.create_tile_group(dragon_layout,'boss')

        self.sky = Sky()

    def create_tile_group(self,layout,type):
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index,val in enumerate(row):
                if val != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size

                    if type == 'terrain':
                        terrain_tile_list = import_cut_graphic("../levels/terrain_tiles.png")
                        tile_surface = terrain_tile_list[int(val)]
                        sprite = StaticTile(tile_size,x,y,tile_surface)

                    if type == 'torch':
                        sprite = Torch(tile_size,x,y)

                    if type == 'enemies':
                        sprite = Enemy(tile_size,x,y)

                    if type == 'constraints':
                        sprite = Tile(tile_size,x,y)

                    if type == 'boss':
                        sprite = Dragon(3*tile_size,x,y)    
                    
                    sprite_group.add(sprite)

        return sprite_group  

    def player_setup(self,layout,change_health):
        for row_index, row in enumerate(layout):
                for col_index,val in enumerate(row):
                    x = col_index * tile_size
                    y = row_index * tile_size
                    if val == '0':
                        sprite = Player((x,y),self.display_surface, change_health)
                        self.player.add(sprite)

                    if val =='1':
                        sign_surface = pygame.image.load("../levels/signExit.png").convert_alpha()
                        sprite = StaticTile(tile_size,x,y,sign_surface)
                        self.goal.add(sprite)

    def enemy_collision_reverse(self):
        for enemy in self.enemies_sprites.sprites():
            if pygame.sprite.spritecollide(enemy,self.constraint_sprites,False):
                enemy.reverse()

    def dragon_collision_reverse(self):
        for dragon in self.dragon_sprites.sprites():
            if pygame.sprite.spritecollide(dragon,self.constraint_sprites,False):
                dragon.reverse()  

    def horizontal_movement_collision(self): #Funçao que define a funcionalidade das colisões horizontais
        player = self.player.sprite

        player.rect.x += player.direction.x * player.speed

        collidable_sprites = self.terrain_sprites.sprites()

        for sprite in collidable_sprites:
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right
        
        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
            player.on_right = False

    def vertical_movement_collision(self): #Funçao que define a funcionalidade das colisões verticais
        player = self.player.sprite
        player.apply_gravity()
        collidable_sprites = self.terrain_sprites.sprites()

        for sprite in collidable_sprites:
            if sprite.rect.colliderect(player.rect):
                if player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True
                elif player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
            
        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False      

    def scroll_x(self): #Função que define a funcionalidade da câmera
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        keys = pygame.key.get_pressed()

        if player_x <= screen_width / 4 and direction_x < 0 and keys[pygame.K_LSHIFT]:
            self.world_shift = 10
            player.speed = 0
        elif player_x >= screen_width - (screen_width / 4) and direction_x > 0 and keys[pygame.K_LSHIFT]:
            self.world_shift = -10
            player.speed = 0
        elif player_x < screen_width / 4 and direction_x < 0: 
            self.world_shift = 6
            player.speed = 0
        elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
            self.world_shift = -6
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 6
    

    def check_death(self):
       if self.player.sprite.rect.top > screen_height:
        self.create_overworld(self.current_level,0)

    def check_win(self):
        if pygame.sprite.spritecollide(self.player.sprite,self.goal,False):
            self.create_overworld(self.current_level,self.new_max_level)

    def check_enemy_collision(self,enemy):
        enemy_collisions = pygame.sprite.spritecollide(self.player.sprite,enemy,False)

        if enemy_collisions:
            for enemy in enemy_collisions:
                for enemy in enemy_collisions:
                    enemy_center = enemy.rect.centery
                    enemy_top = enemy.rect.top
                    player_bottom = self.player.sprite.rect.bottom
                    if enemy_top < player_bottom < enemy_center:
                        self.player.sprite.direction.y = -15
                        self.player.sprite.get_damage()
                    else:
                        self.player.sprite.get_damage()              
 

    def run(self):      

        self.sky.draw(self.display_surface)

        self.terrain_sprites.draw(self.display_surface)
        self.terrain_sprites.update(self.world_shift)

        self.torch_sprites.draw(self.display_surface)
        self.torch_sprites.update(self.world_shift)

        self.enemies_sprites.draw(self.display_surface)
        self.constraint_sprites.update(self.world_shift)
        self.enemy_collision_reverse()
        self.enemies_sprites.update(self.world_shift)

        self.dragon_sprites.draw(self.display_surface)
        self.dragon_collision_reverse()
        self.dragon_sprites.update(self.world_shift)

        self.player.update(self.terrain_sprites,self.enemies_sprites,self.dragon_sprites)
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.scroll_x()
        self.player.draw(self.display_surface)
        self.goal.update(self.world_shift)
        self.goal.draw(self.display_surface)

        self.check_death()
        self.check_win()

        self.check_enemy_collision(self.enemies_sprites)
        self.check_enemy_collision(self.dragon_sprites)