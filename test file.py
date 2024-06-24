import pygame
import sys
import random
import time
import mark_module

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

imageunharmed = pygame.image.load("sprites/download-Photoroom.png")
pygame.transform.scale(imageunharmed, (.1,.1), 1)
while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((255, 255, 255))
        screen.blit(imageunharmed, (0, 0))
        pygame.display.update()

main()