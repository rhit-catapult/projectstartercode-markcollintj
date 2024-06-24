import pygame
import sys
import random
import time
# need counsalur imagise (mabye as caricter salection) tj on free time
# need player charicter
# need projectile: Mark
# need enemy
# need level/location



def main():
    # turn on pygame
    pygame.init()

    # create a screen
    pygame.display.set_caption("Cool Project")
    # TODO: Change the size of the screen as you see fit!
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    # let's set the framerate
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_p]:
            sys.exit()

            # TODO: Add you events code

        # TODO: Fill the screen with whatever background color you like!
        screen.fill((255, 255, 255))

        # TODO: Add your project code


        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()

main()
