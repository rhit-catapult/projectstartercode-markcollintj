import pygame
import sys
import random
import time
import mark_module

class Menu:
    def __init__(self, screen: pygame.Surface, x , y):
        self.screen = screen
        self.x = x
        self.y = y




pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
font1 = pygame.font.SysFont("[pmingliuextb]",70)

Menu1 = pygame.image.load("sprites/Menu.png")

#caption1 = font1.render("The Grasshole Apocolapse", True, (23, 13, 163))

while True:

        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_p]:
            sys.exit()

        screen.blit(Menu1, (screen.get_width()/2-250, screen.get_height()/2-250))

        pygame.display.update()

main()