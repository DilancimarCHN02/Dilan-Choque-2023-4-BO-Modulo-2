import pygame
from pygame.sprite import Sprite
from game.components.power_ups.power_up import PowerUp
from game.utils.constants import DUPLICATE_SHIP, DUPLICATE_SHIP_TYPE
from game.components.spaceship import Spaceship


class Duplicate_ship(PowerUp):
    def __init__(self):
        super().__init__(DUPLICATE_SHIP, DUPLICATE_SHIP_TYPE)
       
