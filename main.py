import pygame
from random import randrange

pygame.init()

size = w, h = 400, 300
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

balls = []
v = 100
fps = 60

running = True
while running:
    screen.fill((0, 0, 0))
    for center, color in balls:
        center[1] = center[1] + v // fps if center[1] < 290 else 290
        pygame.draw.circle(screen, color, center, 10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            color = pygame.Color(randrange(256), randrange(256), randrange(256))
            pygame.draw.circle(screen, color, event.pos, 10)
            balls.append((list(event.pos), color))

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
