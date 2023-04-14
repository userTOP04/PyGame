
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
recatangle_width = 50
recatangle_height = 50
recatangle_x = screen.get_width() / 2 - recatangle_width // 2
recatangle_y = screen.get_height() / 2 - recatangle_height // 2
recatangle = pygame.Rect(
    recatangle_x,
    recatangle_y,
    recatangle_width,
    recatangle_height
) #X #Y #ширина #высота
recatangle_color = (255, 255, 255) #Red #Green #Blue
pygame.draw.rect(screen, recatangle_color, recatangle, 0)


while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get(): #сбор событий в "список"
        if event.type == pygame.QUIT: #разбор событий
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        recatangle.y -= 1
    if keys[pygame.K_DOWN]:
        recatangle.y += 1
    if keys[pygame.K_LEFT]:
        recatangle.x -= 1
    if keys[pygame.K_RIGHT]:
        recatangle.x += 1


    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, recatangle_color, recatangle)
    pygame.display.flip() #переворот доски(загрузка)