import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, DEFAULT_TYPE, SPACESHIP_SPEED_TYPE,LASER_PATH
from game.components.bullets.bullet_manager import BulletManager
from game.components.bullets.bullet import Bullet

class Spaceship(Sprite):


    SHIP_WIDTH = 40
    SHIP_HEIGHT = 60
    X_POS = (SCREEN_WIDTH // 2) - SHIP_WIDTH
    Y_POS = 500
    SHIP_SPEED = 10
    

    
    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image,(40,60))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.angle = 0
        self.total_deaths = 0 
        self.type = 'player'    
        self.power_up_type = DEFAULT_TYPE
        self.has_power_up = False
        self.is_firing = False
        self.power_time_up = 0
        self.ship_speed = 10
        



    def update(self, user_input, game):
    
        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_UP]:
            self.move_up()
        elif user_input[pygame.K_DOWN]:
            self.move_down()
        

        if user_input[pygame.K_q]:
            self.turn_left()
        if user_input[pygame.K_e]:
            self.turn_right()
        if user_input[pygame.K_w]:
            self.shoot(game)


    def move_left(self):
        self.rect.x -= self.ship_speed  
        if self.rect.left < 0:
             self.rect.x = SCREEN_WIDTH - self.ship_speed

    def move_right(self):
        self.rect.x += self.ship_speed  
        if self.rect.left >= SCREEN_WIDTH - self.ship_speed:
             self.rect.x = 0                  

    def move_up(self):
         if self.rect.y > SCREEN_HEIGHT // 2:
              self.rect.y -= self.ship_speed
         
    def move_down(self):
         if self.rect.y < SCREEN_HEIGHT - 70:
              self.rect.y += self.ship_speed

    def turn_left(self):
        self.angle += 15

    def turn_right(self):
        self.angle -= 15


    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.image, self.angle)  
        new_rect = rotated_image.get_rect(center = self.rect.center)
        screen.blit(rotated_image, new_rect)

    
    def shoot(self,game): 
        bullet = Bullet(self)
        game.bullet_manager.add_bullet(bullet)


    def reset(self):
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

    def set_image(self, size = (SHIP_WIDTH,SHIP_HEIGHT),image = SPACESHIP):
        self.image = image
        self.image = pygame.transform.scale(self.image, size)

    def reset_image(self):
        self.set_image( size = (Spaceship.SHIP_WIDTH, Spaceship.SHIP_HEIGHT), image = SPACESHIP)
        

