import pygame
import sys
import random
import time
import Hero_Module
import mark_module


# need counsalur imagise (mabye as caricter salection) tj on free time
# need player charicter
# need projectile
# need enemy tj
# need level/location


class Cammperhealthy:
    def __init__(self, screen, x, y,):
        self.screen = screen
        self.x = x
        self.y = y
        self.speedx = 3((Hero_Module.Hero.self.x - self.x)/(abs(Hero_Module.Hero.self.x- self.x)))
        self.speedy = 3((Hero_Module.Hero.self.y - self.y)/(abs(Hero_Module.Hero.self.y- self.y)))
        self.imageunharmed = pygame.image.load("sprites/download-Photoroom.png")
        self.imageunharmedright = pygame.image.load("sprites/download-Photoroom.png")
        self.imageunharmedleft =pygame.image.load("sprites/download-Photoroom.png")
        self.imageunharmedup =pygame.image.load("sprites/download-Photoroom.png")
        self.imageunharmeddown =pygame.image.load("sprites/download-Photoroom.png")
        self.imageunharmedleftdown =pygame.image.load("sprites/download-Photoroom.png")
        self.imageunharmedleftup =pygame.image.load("sprites/download-Photoroom.png")
        self.imageunharmedrightup =pygame.image.load("sprites/download-Photoroom.png")
        self.imageunharmedrightdown =pygame.image.load("sprites/download-Photoroom.png")
        self.projectilehits =0

    def move(self):
        self.x = self.x + self.speedx
        self.x = self.y + self.speedy


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
class Cammperhurt:
    def __init__(self, screen, x, y, ):
        self.screen = screen
        self.x = x
        self.y = y
        self.speedx = 1.5((Hero_Module.Hero.self.x - self.x)/(abs(Hero_Module.Hero.self.x- self.x)))
        self.speedy = 1.5((Hero_Module.Hero.self.y - self.y)/(abs(Hero_Module.Hero.self.y- self.y)))
        self.imageharmed =pygame.image.load("sprites/download-Photoroom.png")
        self.imageharmedright =pygame.image.load("sprites/download-Photoroom.png")
        self.imageharmedleft =pygame.image.load("sprites/download-Photoroom.png")
        self.imageharmedup =pygame.image.load("sprites/download-Photoroom.png")
        self.imageharmeddown =pygame.image.load("sprites/download-Photoroom.png")
        self.imageharmedleftdown =pygame.image.load("sprites/download-Photoroom.png")
        self.imageharmedleftup =pygame.image.load("sprites/download-Photoroom.png")
        self.imageharmedrightup =pygame.image.load("sprites/download-Photoroom.png")
        self.imageharmedrightdown =pygame.image.load("sprites/download-Photoroom.png")
        self.projectilehits =1


    def move(self):
        self.x = self.x + self.speedx
        self.y = self.y + self.speedy

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
class Cammperdead:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.imagedead =pygame.image.load("sprites/download-Photoroom.png")

        self.projectilehits =2





    def draw(self):

            self.screen.blit(self.imagedead, (self.x, self.y))








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
    hurt = []
    healthy = []
    dead = []
    round = clock / 10
    spawns = round*5
    if clock%10:
        spawnernumber = random.randint(0, "spawns")
        waveside = random.randint(1,4)
        if waveside == 1:
            spawnsidex = 0
            spawnsidey = 0
        if waveside == 2:
            spawnsidex = 0
            spawnsidey = 0
        if waveside == 3:
            spawnsidex = 0
            spawnsidey = 0
        if waveside == 4:
            spawnsidex = 0
            spawnsidey = 0
        for i in range(1, spawnernumber):
            camperhurt = Cammperhurt(screen, (Cammperhealthy.self.x, Cammperhealthy.self.y), )
            hurt.append(camperhurt)
        for i in range(1, (spawns-spawnernumber)/2):
            camperhealthy = Cammperhealthy(screen, (spawnsidex, spawnsidey))
            healthy.append(camperhealthy)
    if mark_module.Projectile.___ >= Cammperhealthy.self.x and mark_module.Projectile.___ <= Cammperhealthy.self.x + self.imagedead.get_width(Cammperhealthy) and mark_module.Projectile.___ >= Cammperhealthy.self.y and mark_module.Projectile.___ <= Cammperhealthy.self.y + self.imagedead.get_hight(Cammperhealthy):
        for i in range(1,1):
            hurtcamper = Cammperhurt(screen, (Cammperhealthy.self.x, Cammperhealthy.self.y), )
            hurt.append(hurtcamper)
            healthy.remove()
    if mark_module.Projectile.___ >= Cammperhurt.self.x and mark_module.Projectile.___ <= Cammperhurt.self.x + self.imagedead.get_width() and mark_module.Projectile.___ >= Cammperhurt.self.y and mark_module.Projectile.___ <= Cammperhurt.self.y + self.imagedead.get_hight(Cammperhurt):
        for i in range(1, len(dead)):
            camperdead = Cammperdead(screen, (Cammperhurt.self.x, Cammperhurt.self.y) )
            dead.append(camperdead)
            hurt.remove()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        clock.tick(60)

            # TODO: Add you events code
        for camperhurt in hurt:
            camperhurt.move()
            camperhurt.draw()
        for camperhealthy in healthy:
            camperhealthy.move()
            camperhealthy.draw()
        for cammperdead in dead:
            cammperdead.draw()
        for hurtcamper in hurt:
            hurtcamper.move()
            hurtcamper.draw()
        # TODO: Fill the screen with whatever background color you like!
        screen.fill((255, 255, 255))

        # TODO: Add your project code

        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()


if __name__ == "__main__":
    main()