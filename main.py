import pygame
from random import randrange

res = 800
size = 50

x,y = randrange(0, res, size), randrange(0, res, size)
apple = randrange(0, res, size), randrange(0, res, size)
lenght = 1
snake = [(x,y)]
dx, dy = 0, 0
fps = 5

pygame.init()

sc = pygame.display.set_mode([res, res])
clock = pygame.time.Clock()

while True:
    sc.fill(pygame.Color('black'))
    [(pygame.draw.rect(sc, pygame.Color('green'), (i, j, size, size))) for i, j, in snake]
    pygame.draw.rect(sc, pygame.Color('red'), (*apple, size, size))

    x += dx * size
    y += dy * size
    snake.append((x, y))
    snake = snake[-lenght:]

    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        dx, dy = 0, -1
    if key[pygame.K_s]:
        dx, dy = 0, 1
    if key[pygame.K_a]:
        dx, dy = -1, 0
    if key[pygame.K_d]:
        dx, dy = 1, 0