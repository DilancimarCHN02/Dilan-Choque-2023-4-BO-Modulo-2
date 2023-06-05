import random
import pygame

from game.components.power_ups.speedPowerUp import SpeedPowerUp
from game.components.power_ups.duplicate_ship import Duplicate_ship           ## para el lunes
from game.components.power_ups.shield import Shield
from game.components.bullets.bullet_manager import BulletManager
from game.utils.constants import SPACESHIP_SHIELD, SPACESHIP_SPEED, DUPLICATE_SHIP,SHIELD_TYPE, SPACESHIP,SPACESHIP_SPEED_TYPE, DUPLICATE_SHIP_TYPE


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(5000, 10000)
        self.duration = random.randint(3, 5)

    def generate_power_up(self):
        power_up = random.choice([Shield(), Duplicate_ship(),SpeedPowerUp()])   # random en una lsita de los power_ups
        self.when_appears += random.randint(5000,10000)
        self.power_ups.append(power_up)


    def update(self, game):
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)

            if game.player.rect.colliderect(power_up.rect):
                if power_up.type == SHIELD_TYPE:
                    power_up.start_time = pygame.time.get_ticks()
                    game.player.power_up_type = power_up.type
                    game.player.has_power_up = True
                    game.player.power_time_up = power_up.start_time + (self.duration *1000)
                    game.player.set_image((65, 75), SPACESHIP_SHIELD)
               
                elif power_up.type == SPACESHIP_SPEED_TYPE:                           # cuando es de tipo speed
                    power_up.start_time = pygame.time.get_ticks()
                    game.player.power_up_type = power_up.type
                    game.player.has_power_up = True
                    game.player.power_time_up = power_up.start_time + (self.duration *1000)
                    game.player.set_image((40,60), SPACESHIP)
                    game.player.ship_speed = 30
            

                else:
                    game.player.set_image((40,60), SPACESHIP)
                self.power_ups.remove(power_up)
                
  

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset(self):
        self.power_ups = []
        now = pygame.time.get_ticks()
        self.when_appears = random.randint(now + 5000, now + 10000)
