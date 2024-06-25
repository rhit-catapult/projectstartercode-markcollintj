import pygame
import sys
import random
import time
import Hero_Module
import mark_module
import math


# need counsalur imagise (mabye as caricter salection) tj on free time
# need player charicter
# need projectile
# need enemy tj
# need level/location


class Cammperhealthy:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.imageunharmed = pygame.image.load("sprites/download-Photoroom.png")
        self.imageunharmedright = pygame.image.load("sprites/download-Photoroom.png")
        self.imageunharmedleft = pygame.image.load("sprites/download-Photoroom.png")
        self.imageunharmedup =pygame.image.load("sprites/download-Photoroom.png")
        self.imageunharmeddown = pygame.image.load("sprites/download-Photoroom.png")
        self.imageunharmedleftdown = pygame.image.load("sprites/download-Photoroom.png")
        self.imageunharmedleftup = pygame.image.load("sprites/download-Photoroom.png")
        self.imageunharmedrightup = pygame.image.load("sprites/download-Photoroom.png")
        self.imageunharmedrightdown = pygame.image.load("sprites/download-Photoroom.png")
        self.hit_box_unharmed_left = pygame.draw.rect()

    def move(self):
        self.speedx = 3 * ((Hero_Module.Hero.x - self.x) / (abs(Hero_Module.Hero.x - self.x)))
        self.speedy = 3 * ((Hero_Module.Hero.y - self.y) / (abs(Hero_Module.Hero.y - self.y)))
        self.x = self.x + self.speedx
        self.x = self.y + self.speedy


    def draw(self):
        self.speedx = 3 * ((Hero_Module.Hero.x - self.x) / (abs(Hero_Module.Hero.x - self.x)))
        self.speedy = 3 * ((Hero_Module.Hero.y - self.y) / (abs(Hero_Module.Hero.y - self.y)))
        if self.speedx == 0 and self.speedy == 0:
            self.screen.blit(self.imageunharmed, (self.x, self.y))
        elif self.speedx >= 0 and self.speedy == 0:
            self.screen.blit(self.imageunharmedright, (self.x, self.y))
        elif self.speedx <= 0 and self.speedy == 0:
            self.screen.blit(self.imageunharmedleft, (self.x, self.y))
        elif self.speedx == 0 and self.speedy >= 0:
            self.screen.blit(self.imageunharmeddown, (self.x, self.y))
        elif self.speedx == 0 and self.speedy <= 0:
            self.screen.blit(self.imageunharmedup, (self.x, self.y))
        elif self.speedx >= 0 and self.speedy >= 0:
            self.screen.blit(self.imageunharmedleftdown, (self.x, self.y))
        elif self.speedx <= 0 and self.speedy >= 0:
            self.screen.blit(self.imageunharmedrightdown, (self.x, self.y))
        elif self.speedx >= 0 and self.speedy <= 0:
            self.screen.blit(self.imageunharmedleftup, (self.x, self.y))
        else:
            self.screen.blit(self.imageunharmedrightup, (self.x, self.y))

        def hitby():
            self.speedx = 3 * ((Hero_Module.Hero.x - self.x) / (abs(Hero_Module.Hero.x - self.x)))
            self.speedy = 3 * ((Hero_Module.Hero.y - self.y) / (abs(Hero_Module.Hero.y - self.y)))
            if self.speedx == 0 and self.speedy == 0:
                self.hit_box = pygame.Rect(self.x, self.y, self.imageunharmed.get_width(),
                                           self.imageunharmed.get_height())
            elif self.speedx >= 0 and self.speedy == 0:
                self.hit_box = pygame.Rect(self.x, self.y, self.imageunharmedright.get_width(),
                                           self.imageunharmedright.get_height())
            elif self.speedx <= 0 and self.speedy == 0:
                self.hit_box = pygame.Rect(self.x, self.y, self.imageunharmedleft.get_width(),
                                           self.imageunharmedleft.get_height())
            elif self.speedx == 0 and self.speedy >= 0:
                self.hit_box = pygame.Rect(self.x, self.y, self.imageunharmeddown.get_width(),
                                self.imageunharmeddown.get_height())
            elif self.speedx == 0 and self.speedy <= 0:
                self.hit_box = pygame.Rect(self.x, self.y, self.imageunharmedup.get_width(),
                                self.imageunharmedup.get_height())
            elif self.speedx >= 0 and self.speedy >= 0:
                self.hit_box = pygame.Rect(self.x, self.y, self.imageunharmedleftdown.get_width(),
                                           self.imageunharmedleftdown.get_height())
            elif self.speedx <= 0 and self.speedy >= 0:
                self.hit_box = pygame.Rect(self.x, self.y, self.imageunharmedrightdown.get_width(),
                                 self.imageunharmedrightdown.get_height())
            elif self.speedx >= 0 and self.speedy <= 0:
                self.hit_box = pygame.Rect(self.x, self.y, self.imageunharmedleftup.get_width(),
                                           self.imageunharmedleftup.get_height())
            else:
                self.hit_box = pygame.Rect(self.x, self.y, self.imageunharmedrightup.get_width(),
                                           self.imageunharmedrightup.get_width())


class Cammperhurt:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.imageharmed = pygame.image.load("sprites/download-Photoroom.png")
        self.imageharmedright = pygame.image.load("sprites/download-Photoroom.png")
        self.imageharmedleft = pygame.image.load("sprites/download-Photoroom.png")
        self.imageharmedup = pygame.image.load("sprites/download-Photoroom.png")
        self.imageharmeddown = pygame.image.load("sprites/download-Photoroom.png")
        self.imageharmedleftdown = pygame.image.load("sprites/download-Photoroom.png")
        self.imageharmedleftup = pygame.image.load("sprites/download-Photoroom.png")
        self.imageharmedrightup = pygame.image.load("sprites/download-Photoroom.png")
        self.imageharmedrightdown = pygame.image.load("sprites/download-Photoroom.png")


    def move(self):
        self.x = self.x + 1.5 * ((Hero_Module.Hero.x - self.x)/(abs(Hero_Module.Hero.x - self.x)))
        self.y = self.y + 1.5 * ((Hero_Module.Hero.y - self.y)/(abs(Hero_Module.Hero.y - self.y)))

    def draw(self):
        self.speedx = 1.5 * ((Hero_Module.Hero.x - self.x)/(abs(Hero_Module.Hero.x - self.x)))
        self.speedy = 1.5 * ((Hero_Module.Hero.y - self.y)/(abs(Hero_Module.Hero.y - self.y)))
        if self.speedx == 0 and self.speedy == 0:
            self.screen.blit(self.imageharmed, (self.x, self.y))
        elif self.speedx >= 0 and self.speedy == 0:
            self.screen.blit(self.imageharmedright, (self.x, self.y))
        elif self.speedx <= 0 and self.speedy == 0:
            self.screen.blit(self.imageharmedleft, (self.x, self.y))
        elif self.speedx == 0 and self.speedy >= 0:
            self.screen.blit(self.imageharmeddown, (self.x, self.y))
        elif self.speedx == 0 and self.speedy <= 0:
            self.screen.blit(self.imageharmedup, (self.x, self.y))
        elif self.speedx >= 0 and self.speedy >= 0:
            self.screen.blit(self.imageharmedleftdown, (self.x, self.y))
        elif self.speedx <= 0 and self.speedy >= 0:
            self.screen.blit(self.imageharmedrightdown, (self.x, self.y))
        elif self.speedx >= 0 and self.speedy <= 0:
            self.screen.blit(self.imageharmedleftup, (self.x, self.y))
        elif self.speedx <= 0 and self.speedy <= 0:
            self.screen.blit(self.imageharmedrightup, (self.x, self.y))

class Cammperdead:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.imagedead = pygame.image.load("sprites/download-Photoroom.png")





    def draw(self):

            self.screen.blit(self.imagedead, (self.x, self.y))





def main():
    # turn on pygame
    pygame.init()

    # create a screen
    pygame.display.set_caption("Cool Project")
    # TODO: Change the size of the screen as you see fit!
    screen = pygame.display.set_mode((640, 480))
    width = screen.get_width()
    height = screen.get_height()
    # let's set the framerate
    clock = pygame.time.Clock()
    clock2 = 0
    hurt = []
    healthy = []
    dead = []


    # for
    #     if Cammperhealthy.hitby(mark_module.Projectile):
    #     hurtcamper = Cammperhurt(screen, (Cammperhealthy.self.x, Cammperhealthy.self.y), )
    #     hurt.append(hurtcamper)
    #     healthy.remove()
    # if Cammperhurt.hitby(mark_module.Projectile):
    #     for i in range(1, len(dead)):
    #         camperdead = Cammperdead(screen, (Cammperhurt.self.x, Cammperhurt.self.y) )
    #         dead.append(camperdead)
    #         hurt.remove()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        clock.tick(60)

        if not (time.time() - clock2) % 10:
            spawns = math.floor((time.time() - clock2) / 2)
            spawnernumber = random.randint(0, spawns)
            waveside = random.randint(1, 4)
            if waveside == 1:
                for i in range(0, spawnernumber):
                    camperhurt = Cammperhurt(screen, random.randint(1, width), 1)
                    hurt.append(camperhurt)
                    spawnernumber -= 1
                for i in range(0, math.floor(spawnernumber / 2)):
                    camperhealthy = Cammperhealthy(screen, random.randint(0, width), 0)
                    healthy.append(camperhealthy)
            elif waveside == 2:
                for i in range(0, spawnernumber):
                    camperhurt = Cammperhurt(screen, random.randint(1, width), height)
                    hurt.append(camperhurt)
                    spawnernumber -= 1
                for i in range(0, math.floor(spawnernumber / 2)):
                    camperhealthy = Cammperhealthy(screen, random.randint(1, width), height)
                    healthy.append(camperhealthy)
            elif waveside == 3:
                for i in range(0, spawnernumber):
                    camperhurt = Cammperhurt(screen, 0, random.randint(0, height))
                    hurt.append(camperhurt)
                    spawnernumber -= 1
                for i in range(0, math.floor(spawnernumber / 2)):
                    camperhealthy = Cammperhealthy(screen, 0, random.randint(0, height))
                    healthy.append(camperhealthy)
            else:
                for i in range(0, spawnernumber):
                    camperhurt = Cammperhurt(screen, width, random.randint(0, height))
                    hurt.append(camperhurt)
                    spawnernumber -= 1
                for i in range(0, math.floor(spawnernumber / 2)):
                    camperhealthy = Cammperhealthy(screen, width, random.randint(0, height))
                    healthy.append(camperhealthy)
            # TODO: Add you events code
        for camperhurt in hurt:
            for bullet in mark_module.projectiles:
                if camperhurt.hitby()
                    cammperdead = Cammperdead(screen, (camperhurt.x, camperhurt.y))
                    dead.append(cammperdead)
                    camperhurt.remove()
                    bullet.remove()
                else:
                    camperhurt.move()
                    camperhurt.draw()
        for camperhealthy in healthy:
            for bullet in mark_module.projectiles:
                if camperhealthy.hitby(bullet):
                    camperhurt = Cammperhurt(screen, (camperhealthy.x, camperhealthy.y))
                    hurt.append(camperhurt)
                    camperhealthy.remove()
                    bullet.remove()
                else:
                    camperhealthy.move()
                    camperhealthy.draw()
        for cammperdead in dead:
            cammperdead.draw()
        # TODO: Fill the screen with whatever background color you like!
        screen.fill((255, 255, 255))

        # TODO: Add your project code

        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()


if __name__ == "__main__":
    main()