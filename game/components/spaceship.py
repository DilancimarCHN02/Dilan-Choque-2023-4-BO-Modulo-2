import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, BULLET
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
        self.type = 'player'


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
        self.rect.x -= self.SHIP_SPEED  
        if self.rect.left <0:
             self.rect.x =SCREEN_WIDTH - self.SHIP_SPEED

    def move_right(self):
        self.rect.x += self.SHIP_SPEED  
        if self.rect.left >= SCREEN_WIDTH - self.SHIP_SPEED:
             self.rect.x = 0                  

    def move_up(self):
         if self.rect.y > SCREEN_HEIGHT // 2:
              self.rect.y -= self.SHIP_SPEED
         
    def move_down(self):
         if self.rect.y < SCREEN_HEIGHT - 70:
              self.rect.y += self.SHIP_SPEED

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

