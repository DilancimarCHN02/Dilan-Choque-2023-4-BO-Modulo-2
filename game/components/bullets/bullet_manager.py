import pygame.mixer
from game.utils.constants import SHIELD_TYPE,EXPLISION_0, EXPLISION_1, EXPLISION_2, EXPLISION_3, EXPLISION_4, EXPLISION_5, EXPLISION_6, EXPLISION_7, EXPLISION_8,EXPLOSION_PATH,LASER_PATH

EXPLOSION_IMAGES = [EXPLISION_0, EXPLISION_1, EXPLISION_2, EXPLISION_3, EXPLISION_4, EXPLISION_5, EXPLISION_6, EXPLISION_7, EXPLISION_8]

class BulletManager:
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []
        self.laser_sound = pygame.mixer.Sound(LASER_PATH)
        self.explosion_sound = pygame.mixer.Sound(EXPLOSION_PATH)
        #pygame.mixer.set_num_channels(10)


    def update(self, game):

        for bullet in self.bullets:
            bullet.update(self.bullets)     

            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and bullet.owner =='player':
                    game.enemy_manager.enemies.remove(enemy)
                    game.score.update()
                    self.bullets.remove(bullet)
                          # Reproducir la animación de explosión                   ##################################
                    explosion_x = enemy.rect.x - enemy.rect.width // 2
                    explosion_y = enemy.rect.y - enemy.rect.height // 2
                    explosion_start_time = pygame.time.get_ticks()
                    frame_duration = 100  # Duración de cada imagen de explosión en milisegundos
                    current_frame = 0
                    while current_frame < len(EXPLOSION_IMAGES):
                        current_time = pygame.time.get_ticks()
                        if current_time - explosion_start_time >= frame_duration:
                            game.screen.blit(EXPLOSION_IMAGES[current_frame], (explosion_x, explosion_y))
                            current_frame += 1
                            explosion_start_time = current_time
                        pygame.display.flip()
                        pygame.event.pump()
                    # sonido ecplosion
                    self.explosion_sound.play()
                
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)


            if bullet.rect.colliderect(game.player.rect) and bullet.owner =='enemy':
                self.enemy_bullets.remove(bullet)
                if game.player.power_up_type != SHIELD_TYPE:
                  game.death_count.update()
                  game.playing = False
                  pygame.time.delay(1000)
                break


    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)
         
        
        for bullet in self.enemy_bullets:
            bullet.draw(screen)



    def add_bullet(self, bullet):
        if bullet.owner == 'player' and len (self.bullets) < 5:                               
            self.laser_sound.play()                          # sonido laser
            self.bullets.append(bullet)
        
        elif bullet.owner == 'enemy' and len (self.enemy_bullets) < 1:
            self.enemy_bullets.append(bullet)

     
    def reset(self):
        self.bullets = []
        self.enemy_bullets = []
