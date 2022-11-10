import pygame
from random import randrange
res1 = 800
res2 = 800
size = 30

x,y = randrange(0, res2, size), randrange(0, res2, size)
apple = randrange(0, res2, size), randrange(0, res2, size)
dirs = {'UP': True, 'DOWN': True, 'LEFT': True, 'RIGHT': True, }
lenght = 1
snake = [(x,y)]
dx, dy = 0, 0
score = 0
fps = 5

pygame.init()

sc = pygame.display.set_mode([res1, res2])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 70, bold=True)
img = pygame.image.load('image.jpg').convert()

while True:
    sc.blit(img, (0, 0))

    [(pygame.draw.rect(sc, pygame.Color('green'), (i, j, size - 2, size - 2))) for i, j, in snake]
    pygame.draw.rect(sc, pygame.Color('red'), (*apple, size, size))

    render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
    sc.blit(render_score, (5, 5))

    x += dx * size
    y += dy * size
    snake.append((x, y))
    snake = snake[-lenght:]

    if snake[-1]  == apple:
        apple = randrange(0, res2, size), randrange(0, res2, size)
        lenght += 1
        score +=1
        fps += 1

    if x < 0 or x > res2 - size or y < 0 or y > res2 - size or len(snake) != len(set(snake)):
        while True:
            render_end = font_end.render('GAME OVER', 1, pygame.Color('orange'))
            sc.blit(render_end, (res2 // 2 - 200, res2 // 3))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()


    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and dirs['UP']:
        dx, dy = 0, -1
        dirs = {'UP': True, 'DOWN': False, 'LEFT': True, 'RIGHT': True, }
    if key[pygame.K_DOWN] and dirs['DOWN']:
        dx, dy = 0, 1
        dirs = {'UP': False, 'DOWN': True, 'LEFT': True, 'RIGHT': True, }
    if key[pygame.K_LEFT] and dirs['LEFT']:
        dx, dy = -1, 0
        dirs = {'UP': True, 'DOWN': True, 'LEFT': True, 'RIGHT': False, }
    if key[pygame.K_RIGHT] and dirs['RIGHT']:
        dx, dy = 1, 0
        dirs = {'UP': True, 'DOWN': True, 'LEFT': False, 'RIGHT': True, }