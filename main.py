import pygame, controls
from roscet import Gun

def run():

    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Космические корабли")
    bg_color = (0, 0, 0)
    gun = Gun(screen)


    while True:
        
        controls.events()
        screen.fill(bg_color)
        gun.output()
        pygame.display.flip()

run()