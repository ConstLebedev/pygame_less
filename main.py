import pygame
from random import randrange

pygame.init()

size = w, h = 400, 300
screen = pygame.display.set_mode(size)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            color = pygame.Color(randrange(256), randrange(256), randrange(256))
            pygame.draw.circle(screen, color, event.pos, 10)
    pygame.display.flip()

pygame.quit()