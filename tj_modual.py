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
        self.imageunharmedright = pygame.image.load("sprites/camper healthy right.png")
        self.imageunharmedleft = pygame.image.load("sprites/camper healthy left.png")
        self.imageunharmedup = pygame.image.load("sprites/camper healthy up.png")
        self.imageunharmeddown = pygame.image.load("sprites/camper healthy down.png")
        self.imageunharmedleftdown = pygame.image.load("sprites/camper healthy left down.png")
        self.imageunharmedleftup = pygame.image.load("sprites/camper healthy left up.png")
        self.imageunharmedrightup = pygame.image.load("sprites/camper healthy right up.png")
        self.imageunharmedrightdown = pygame.image.load("sprites/camper healthy right down.png")

    def move(self):
        self.speedx = 3 * ((Hero_Module.Hero.x - self.x) / (abs(Hero_Module.Hero.x - self.x)))
        self.speedy = 3 * ((Hero_Module.Hero.y - self.y) / (abs(Hero_Module.Hero.y - self.y)))
        self.x = self.x + self.speedx
        self.x = self.y + self.speedy


    def draw(self):
        self.speedx = 3 * ((Hero_Module.Hero.x - self.x) / (abs(Hero_Module.Hero.x - self.x)))
        self.speedy = 3 * ((Hero_Module.Hero.y - self.y) / (abs(Hero_Module.Hero.y - self.y)))
        if self.speedx >= 0 and self.speedy == 0:
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

    def hitby(self, Projectile):
        self.speedx = 3 * ((Hero_Module.Hero.x - self.x) / (abs(Hero_Module.Hero.x - self.x)))
        self.speedy = 3 * ((Hero_Module.Hero.y - self.y) / (abs(Hero_Module.Hero.y - self.y)))
        if self.speedx >= 0 and self.speedy == 0:
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
        return self.hit_box.colliderect(Projectile.hit_box)

class Cammperhurt:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.imageharmedright = pygame.image.load("sprites/camper unhealthy right.png")
        self.imageharmedleft = pygame.image.load("sprites/camper unhealthy left.png")
        self.imageharmedup = pygame.image.load("sprites/camper unhealthy up.png")
        self.imageharmeddown = pygame.image.load("sprites/camper unhealthy down.png")
        self.imageharmedleftdown = pygame.image.load("sprites/camper unhealthy left down.png")
        self.imageharmedleftup = pygame.image.load("sprites/camper unhealthy left up.png")
        self.imageharmedrightup = pygame.image.load("sprites/camper unhealthy right up.png")
        self.imageharmedrightdown = pygame.image.load("sprites/camper unhealthy right down.png")


    def move(self):
        self.x = self.x + 1.5 * ((Hero_Module.Hero.x - self.x)/(abs(Hero_Module.Hero.x - self.x)))
        self.y = self.y + 1.5 * ((Hero_Module.Hero.y - self.y)/(abs(Hero_Module.Hero.y - self.y)))

    def draw(self):
        self.speedx = 1.5 * ((Hero_Module.Hero.x - self.x)/(abs(Hero_Module.Hero.x - self.x)))
        self.speedy = 1.5 * ((Hero_Module.Hero.y - self.y)/(abs(Hero_Module.Hero.y - self.y)))
        if self.speedx >= 0 and self.speedy == 0:
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

    def hitby(self, Projectile):
        self.speedx = 3 * ((Hero_Module.Hero.x - self.x) / (abs(Hero_Module.Hero.x - self.x)))
        self.speedy = 3 * ((Hero_Module.Hero.y - self.y) / (abs(Hero_Module.Hero.y - self.y)))
        if self.speedx >= 0 and self.speedy == 0:
            self.hit_box = pygame.Rect(self.x, self.y, self.imageharmedright.get_width(),
                                       self.imageharmedright.get_height())
        elif self.speedx <= 0 and self.speedy == 0:
            self.hit_box = pygame.Rect(self.x, self.y, self.imageharmedleft.get_width(),
                                       self.imageharmedleft.get_height())
        elif self.speedx == 0 and self.speedy >= 0:
            self.hit_box = pygame.Rect(self.x, self.y, self.imageharmeddown.get_width(),
                                       self.imageharmeddown.get_height())
        elif self.speedx == 0 and self.speedy <= 0:
            self.hit_box = pygame.Rect(self.x, self.y, self.imageharmedup.get_width(),
                                       self.imageharmedup.get_height())
        elif self.speedx >= 0 and self.speedy >= 0:
            self.hit_box = pygame.Rect(self.x, self.y, self.imageharmedleftdown.get_width(),
                                               self.imageharmedleftdown.get_height())
        elif self.speedx <= 0 and self.speedy >= 0:
             self.hit_box = pygame.Rect(self.x, self.y, self.imageharmedrightdown.get_width(),
                                               self.imageharmedrightdown.get_height())
        elif self.speedx >= 0 and self.speedy <= 0:
            self.hit_box = pygame.Rect(self.x, self.y, self.imageharmedleftup.get_width(),
                                               self.imageharmedleftup.get_height())
        else:
            self.hit_box = pygame.Rect(self.x, self.y, self.imageharmedrightup.get_width(),
                                       self.imageharmedrightup.get_width())
        return self.hit_box.colliderect(Projectile.hit_box)

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
                if camperhurt.hitby(bullet):
                    cammperdead = Cammperdead(screen, camperhurt.x, camperhurt.y)
                    dead.append(cammperdead)
                    hurt.remove(camperhurt)
                    bullet.remove()
                else:
                    camperhurt.move()
                    camperhurt.draw()
        for camperhealthy in healthy:
            for bullet in mark_module.projectiles:
                if camperhealthy.hitby(bullet):
                    camperhurt = Cammperhurt(screen, camperhealthy.x, camperhealthy.y)
                    hurt.append(camperhurt)
                    healthy.remove(camperhealthy)
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