import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100 # ancho de pantalla
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
# fond new
#rayo 
SPACESHIP_SPEED = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Other/rayo.png")), (70, 80))
SPACESHIP_SPEED_TYPE = 'speed'
#sonido explosion
EXPLOSION_PATH =LASER_PATH = os.path.join(IMG_DIR, "song/explosion.wav")
#laser
LASER_PATH = os.path.join(IMG_DIR, "song/laser.ogg")
#music
MUSIC_PATH = os.path.join(IMG_DIR, "song/music.ogg")
#explo
EXPLISION_0 = pygame.image.load(os.path.join(IMG_DIR, "Explosion/regularExplosion00.png"))
EXPLISION_1 = pygame.image.load(os.path.join(IMG_DIR, "Explosion/regularExplosion01.png"))
EXPLISION_2 = pygame.image.load(os.path.join(IMG_DIR, "Explosion/regularExplosion02.png"))
EXPLISION_3 = pygame.image.load(os.path.join(IMG_DIR, "Explosion/regularExplosion03.png"))
EXPLISION_4 = pygame.image.load(os.path.join(IMG_DIR, "Explosion/regularExplosion04.png"))
EXPLISION_5 = pygame.image.load(os.path.join(IMG_DIR, "Explosion/regularExplosion05.png"))
EXPLISION_6 = pygame.image.load(os.path.join(IMG_DIR, "Explosion/regularExplosion06.png"))
EXPLISION_7 = pygame.image.load(os.path.join(IMG_DIR, "Explosion/regularExplosion07.png"))
EXPLISION_8 = pygame.image.load(os.path.join(IMG_DIR, "Explosion/regularExplosion08.png"))

# para el power_up duplacate_ship
DUPLICATE_SHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/double_spaceship.png"))
DUPLICATE_SHIP_TYPE = 'double_spaceship'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
               

FONT_STYLE = 'freesansbold.ttf'
