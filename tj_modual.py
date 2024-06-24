import pygame
import sys
import random
import time
import Hero_Module
# need counsalur imagise (mabye as caricter salection) tj on free time
# need player charicter
# need projectile
# need enemy tj
# need level/location


class Cammperhealthy:
    def __init__(self, screen, x, y, speedx, speedy, health, state, ):
        self.screen = screen
        self.x = x
        self.y = y
        self.speedx = 3((Hero_Module.Hero.self.x - self.x)/(abs(Hero_Module.Hero.self.x- self.x)))
        self.speedy = 3((Hero_Module.Hero.self.y - self.y)/(abs(Hero_Module.Hero.self.y- self.y)))
        self.imageunharmed = pygame.image.load("sprites/download-Photoroom.png")
        self.imageunharmedright =
        self.imageunharmedleft =
        self.imageunharmedup =
        self.imageunharmeddown =
        self.imageunharmedleftdown =
        self.imageunharmedleftup =
        self.imageunharmedrightup =
        self.imageunharmedrightdown =
        self.projectilehits =0

    def move(self):
        self.x = self.x += self.speedx
        self.x = self.y += self.speedy


    def draw(self):
        if self.projectilehits == 0 and self.speedx == 0 and self.speedy == 0:
            self.screen.blit(self.imageunharmed, (self.x, self.y))
        elif self.projectilehits == 0 and self.speedx >= 0 and self.speedy == 0:
            self.screen.blit(self.imageunharmedright, (self.x, self.y))
        elif self.projectilehits == 0 and self.speedx <= 0 and self.speedy == 0:
            self.screen.blit(self.imageunharmedleft, (self.x, self.y))
        elif self.projectilehits == 0 and self.speedx == 0 and self.speedy >= 0:
            self.screen.blit(self.imageunharmeddown, (self.x, self.y))
        elif self.projectilehits == 0 and self.speedx == 0 and self.speedy <= 0:
            self.screen.blit(self.imageunharmedup, (self.x, self.y))
        elif self.projectilehits == 0 and self.speedx >= 0 and self.speedy >= 0:
            self.screen.blit(self.imageunharmedleftdown, (self.x, self.y))
        elif self.projectilehits == 0 and self.speedx <= 0 and self.speedy >= 0:
            self.screen.blit(self.imageunharmedrightdown, (self.x, self.y))
        elif self.projectilehits == 0 and self.speedx >= 0 and self.speedy <= 0:
            self.screen.blit(self.imageunharmedleftup, (self.x, self.y))
        elif self.projectilehits == 0 and self.speedx <= 0 and self.speedy <= 0:
            self.screen.blit(self.imageunharmedrightup, (self.x, self.y))
class cammperhurt:
    def __init__(self, screen, x, y, speedx, speedy, health, state, ):
        self.screen = screen
        self.x = x
        self.y = y
        self.speedx = 1.5((Hero_Module.Hero.self.x - self.x)/(abs(Hero_Module.Hero.self.x- self.x)))
        self.speedy = 1.5((Hero_Module.Hero.self.y - self.y)/(abs(Hero_Module.Hero.self.y- self.y)))
        self.imageharmed =
        self.imageharmedright =
        self.imageharmedleft =
        self.imageharmedup =
        self.imageharmeddown =
        self.imageharmedleftdown =
        self.imageharmedleftup =
        self.imageharmedrightup =
        self.imageharmedrightdown =

    def move(self):
        self.x = self.x += self.speedx
        self.y = self.y += self.speedy

    def draw(self):
        if self.projectilehits == 1 and self.speedx == 0 and self.speedy == 0:
            self.screen.blit(self.imageharmed, (self.x, self.y))
        elif self.projectilehits == 1 and self.speedx >= 0 and self.speedy == 0:
            self.screen.blit(self.imageharmedright, (self.x, self.y))
        elif self.projectilehits == 1 and self.speedx <= 0 and self.speedy == 0:
            self.screen.blit(self.imageharmedleft, (self.x, self.y))
        elif self.projectilehits == 1 and self.speedx == 0 and self.speedy >= 0:
            self.screen.blit(self.imageharmeddown, (self.x, self.y))
        elif self.projectilehits == 1 and self.speedx == 0 and self.speedy <= 0:
            self.screen.blit(self.imageharmedup, (self.x, self.y))
        elif self.projectilehits == 1 and self.speedx >= 0 and self.speedy >= 0:
            self.screen.blit(self.imageharmedleftdown, (self.x, self.y))
        elif self.projectilehits == 1 and self.speedx <= 0 and self.speedy >= 0:
            self.screen.blit(self.imageharmedrightdown, (self.x, self.y))
        elif self.projectilehits == 1 and self.speedx >= 0 and self.speedy <= 0:
            self.screen.blit(self.imageharmedleftup, (self.x, self.y))
        elif self.projectilehits == 1 and self.speedx <= 0 and self.speedy <= 0:
            self.screen.blit(self.imageharmedrightup, (self.x, self.y))
class cammperdead:
    def __init__(self, screen, x, y, speedx, speedy, health, state, ):
        self.screen = screen
        self.x = x
        self.y = y
        self.speedx = 0
        self.speedy = 0
        self.imagedead =
        self.imagedeadright =
        self.imagedeadleft =
        self.imagedeadup =
        self.imagedeaddown =
        self.imagedeadleftdown =
        self.imagedeadleftup =
        self.imagedeadrightup =
        self.imagedeadrightdown =




    def draw(self):
        if self.projectilehits >= 2 and self.speedx == 0 and self.speedy == 0:
            self.screen.blit(self.imagedead, (self.x, self.y))
        elif self.projectilehits >= 2 and self.speedx >= 0 and self.speedy == 0:
            self.screen.blit(self.imagedeadright, (self.x, self.y))
        elif self.projectilehits >= 2 and self.speedx <= 0 and self.speedy == 0:
            self.screen.blit(self.imagedeadleft, (self.x, self.y))
        elif self.projectilehits >= 2 and self.speedx == 0 and self.speedy >= 0:
            self.screen.blit(self.imagedeaddown, (self.x, self.y))
        elif self.projectilehits >= 2 and self.speedx == 0 and self.speedy <= 0:
            self.screen.blit(self.imagedeadup, (self.x, self.y))
        elif self.projectilehits >= 2 and self.speedx >= 0 and self.speedy >= 0:
            self.screen.blit(self.imagedeadleftdown, (self.x, self.y))
        elif self.projectilehits >= 2 and self.speedx <= 0 and self.speedy >= 0:
            self.screen.blit(self.imagedeadrightdown, (self.x, self.y))
        elif self.projectilehits >= 2 and self.speedx >= 0 and self.speedy <= 0:
            self.screen.blit(self.imagedeadleftup, (self.x, self.y))
        elif self.projectilehits >= 2 and self.speedx <= 0 and self.speedy <= 0:
            self.screen.blit(self.imagedeadrightup, (self.x, self.y))







pygame.transform.scale()
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
        screen.blit(imageunharmed, (0,0))
        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()


if __name__ == "__main__":
    main()