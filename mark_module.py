import pygame
import sys
import random
import time

# class Projectile:
#     #insert a ", x, y" in instances
#     def __init__(self, screen):
#     self.screen = screen
#     # self.x = Hero.x
#     # self.y = Hero.y
#
#     def draw(self):
#         pygame.draw.circle(screen, )
#
#     def move(self):
#
#     def off_screen(self):
#
#
#     def hits(self):
#         projecticle
def main():
    # turn on pygame
    pygame.init()

    # create a screen
    pygame.display.set_caption("Mark's module")
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