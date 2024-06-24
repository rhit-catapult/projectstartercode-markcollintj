import pygame
import sys
import random
import time
import mark_module

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()



while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((255, 255, 255))

        pygame.display.update()

main()