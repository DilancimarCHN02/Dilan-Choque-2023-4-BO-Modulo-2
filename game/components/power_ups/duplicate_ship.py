from game.components.power_ups.power_up import PowerUp
from game.utils.constants import DUPLICATE_SHIP, DUPLICATE_SHIP_TYPE


class Duplicate_ship(PowerUp):
    def __init__(self):
        super().__init__(DUPLICATE_SHIP, DUPLICATE_SHIP_TYPE)
