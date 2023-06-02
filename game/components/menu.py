import pygame
from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT ,SCREEN_WIDTH

class Menu:
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT //2
    HALF_SCREEN_WIDTH = SCREEN_WIDTH //2

    def __init__(self, message, screen):
        screen.fill((255,255,255))
        self.font = pygame.font.Font(FONT_STYLE,30)
        self.text = self.font.render(message, True,(0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)


    def update(self, game):
        pygame.display.update()
        self.handle_events_on_menu(game)


    def draw(self,screen, score, highest_score, total_deaths): ## diccionario
        screen.blit(self.text, self.text_rect )
        self.draw_text(screen,f"Your Score: {score}", 50)
        self.draw_text(screen,f"Higheet Score: {highest_score}", 100)
        self.draw_text(screen,f"Total Deaths: {total_deaths}", 150)
    
    
    def draw_text(self,screen, text, offset):       #asda
        rendered_text = self.font.render(text, True, (0,0,0))
        text_rect = rendered_text.get_rect()
        text_rect.center =(self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + offset)
        screen.blit(rendered_text, text_rect)


    
    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               game.playing = False
               game.running = False
            elif event.type == pygame.KEYDOWN:
                game.run()

    def reset_screen_color(self, screen):
        screen.fill((255,255,255))

    def update_message(self, message):
        self.text = self.font.render(message, True,(0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)

   