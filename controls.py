import pygame
import sys

def events():
    """обработка событий"""

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()