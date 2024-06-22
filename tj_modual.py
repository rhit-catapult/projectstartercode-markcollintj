import pygame
import sys
import random
import time
import Collin_module
# need counsalur imagise (mabye as caricter salection) tj on free time
# need player charicter
# need projectile
# need enemy tj
# need level/location
#
class cammperhealthy:
    def __init__(self, screen, x, y, speedx, speedy, health, state, ):
        self.screen = screen
        self.x = x
        self.y = y
        self.speedx =
        self.speedy =

    def move(self):
        self.

    def draw(self):
        if Projectilehits == 1:
            self.screen.blit(self.image_no_umbrella, (self.x, self.y))
        else :
            self.screen.blit(self.image_umbrella, (self.x, self.y))
class cammperhurt:
    def __init__(self, screen, x, y, speedx, speedy, health, state, ):
        self.screen = screen
        self.x = x
        self.y = y
        self.speedx =
        self.speedy =

    def move(self):
        self.

    def draw(self):
        if self.Projectilehits == 1:
            self.screen.blit(self.image_no_umbrella, (self.x, self.y))
        else :
            self.screen.blit(self.image_umbrella, (self.x, self.y))

class cammperdead:
    def __init__(self, screen, x, y, speedx, speedy, health, state, ):
        self.screen = screen
        self.x = x
        self.y = y
        self.speedx =
        self.speedy =

    def move(self):
        self.

    def draw(self):
        if Projectilehits == 1:
            self.screen.blit(self.image_no_umbrella, (self.x, self.y))
        else :
            self.screen.blit(self.image_umbrella, (self.x, self.y))








def main():
    # turn on pygame
    pygame.init()

    # create a screen
    pygame.display.set_caption("Cool Project")
    # TODO: Change the size of the screen as you see fit!
    screen = pygame.display.set_mode((640, 480))

    # let's set the framerate
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # TODO: Add you events code

        # TODO: Fill the screen with whatever background color you like!
        screen.fill((255, 255, 255))

        # TODO: Add your project code

        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()


if __name__ == "__main__":
    main()