import pygame.mixer

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS ,FONT_STYLE, DEFAULT_TYPE,MUSIC_PATH,LASER_PATH
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_manager import EnemyManager
from game.components.bullets.bullet_manager import BulletManager
from game.components.menu import Menu
from game.components.power_ups.power_up_manager import PowerUpManager
from game.components.counter import Counter
from game.components.power_ups.duplicate_ship import Duplicate_ship
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.paused = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.menu = Menu(self.screen)
        self.power_up_manager = PowerUpManager()
        self.score = Counter()
        self.death_count = Counter()
        self.highest_score = Counter()
        self.duplicate_ship = Duplicate_ship()
 

        pygame.mixer.set_num_channels(10)
        

    
    
    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.reset()
        
        self.playing = True
        self.paused = False
        
        while self.playing:
            if not self.paused:      #estado de pausa DESACTIVADO
                self.events()
                self.update()
                self.draw()
            else: 
                for event in pygame.event.get():           #volver a presionar 
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            self.paused = False
                        elif self.paused:
                            self.handle_paused_events(event)
                        
    def handle_paused_events(self,event):           
        if event.key == pygame.K_a:
            print("Reducing volume")
            current_volume = pygame.mixer.music.get_volume()
            new_volume = max(0.0, current_volume - 0.1)
            self.set_music_volume(new_volume)
        elif event.key == pygame.K_d:
            print("Increasing volume")
            current_volume = pygame.mixer.music.get_volume()
            new_volume = min(1.0, current_volume + 0.1)
            self.set_music_volume(new_volume)
        elif event.key == pygame.K_s:
            print("Toggling music pause")
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.unpause()   

    def set_music_volume(self, volume):
        if volume < 0.0:
            volume = 0.0
        elif volume > 1.0:
            volume = 1.0
        pygame.mixer.music.set_volume(volume)    


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.paused = not self.paused             #cambia estado

    def update(self): 
        if not self.paused:
            user_input = pygame.key.get_pressed()
            self.player.update(user_input, self)
            self.enemy_manager.update(self)
            self.bullet_manager.update(self)
            self.power_up_manager.update(self)


    

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.score.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
        pygame.display.update()
        # pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed   

    def show_menu(self):
        half_screen_height = SCREEN_HEIGHT //2
        half_screen_width = SCREEN_WIDTH //2
        
        self.menu.reset_screen_color(self.screen)

        if self.death_count.count == 0:
            self.menu.draw(self.screen,'Press any key to Start...')
        
        else:
            self.update_highest_score()
            self.menu.draw(self.screen,'Game over. Press any key to start')
            self.menu.draw(self.screen,f"Your Score: {self.score.count}", half_screen_width, 350, )
            self.menu.draw(self.screen,f"Highest Score: {self.highest_score.count}", half_screen_width, 400, )
            self.menu.draw(self.screen,f"Total Deaths: {self.death_count.count}", half_screen_width, 450, )
    

        icon = pygame.transform.scale(ICON,(80,120))
        self.screen.blit(icon,(half_screen_width - 50, half_screen_height - 150))

        self.menu.update(self)                                                          

    def update_highest_score(self):
          if self.score.count > self.highest_score.count:
            self.highest_score.set_count(self.score.count)

    def reset(self):
        self.power_up_manager.reset()
        self.bullet_manager.reset()
        self.enemy_manager.reset()
        self.score.reset()
        self.player.reset()

    
    def draw_power_up_time(self):
        if self.player.has_power_up and not self.paused:        #verifica la pausa su estado 
            if self.player.has_power_up:
                time_to_show = round((self.player.power_time_up - pygame.time.get_ticks())/1000, 2)

                if time_to_show >= 0:
                    self.menu.draw(self.screen, f'{self.player.power_up_type.capitalize()} is enabled for {time_to_show} seconds', 540, 50, (255, 255, 255))
                else:
                    self.player.has_power_up = False
                    self.player.power_up_type = DEFAULT_TYPE
                    self.player.set_image()
                    self.player.ship_speed = self.player.SHIP_SPEED
                     