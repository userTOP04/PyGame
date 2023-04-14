import pygame
import sys

Class Paddle:
    def __init__(self, x):
        self.image = pygame.Surface((20, 70)) # изображение на поверхности
        self.image.fill((225, 225, 225))
        self.rect = self.image.get_rect() # прямоугольник из изображения
        self.rect.x = x
        self.rect.y = 300




Class Ball:
    pass



Class Score:
    pass



Class Game:
    def __init__(self):
        # подготовка
        self.player_1 = Paddle(100)
        self.screen_color = (0, 0, 0)



    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        while True:
            for event in pygame.event.get(): #сбор событий в "список"
                if event.type == pygame.QUIT: #разбор событий
                    pygame.quit()
                    sys.exit()






