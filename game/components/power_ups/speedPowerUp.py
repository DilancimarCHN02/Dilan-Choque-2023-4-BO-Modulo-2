import pygame
from game.components.power_ups.power_up import PowerUp
from game.utils.constants import SPACESHIP_SPEED, SPACESHIP_SPEED_TYPE


class SpeedPowerUp(PowerUp):
    def __init__(self):
        super().__init__(SPACESHIP_SPEED, SPACESHIP_SPEED_TYPE)
 


