import pygame

pygame.init()

size = w, h = 400, 300
screen = pygame.display.set_mode(size)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()