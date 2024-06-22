import pygame
import sys
import random
import time



class Hero:
    def __init__(self, screen: pygame.Surface,x , y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speedx = 5
        self.speedy = 5
        self.raidius = 10
        self.color = pygame.Color("Blue")

    def move(self, xa, ya):

        self.y += ya
        self.x += xa


    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.raidius)



def main():

    pygame.init()


    pygame.display.set_caption("Hero module")

    screen = pygame.display.set_mode((640, 480))
    pressed_keys = pygame.key.get_pressed()
    clock = pygame.time.Clock()

    heros = Hero(screen, random.randint(100,screen.get_width()-100), random.randint(100,screen.get_height()-100))

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # TODO: Add you events code

        screen.fill((255, 255, 255))

        heros.draw()

        if pressed_keys[pygame.K_UP]:
            heros.x -= 5
        if pressed_keys[pygame.K_DOWN]:
            heros.move(0, 5)
        if pressed_keys[pygame.K_LEFT]:
            heros.move(-5, 0)
        if pressed_keys[pygame.K_RIGHT]:
            heros.move(5, 0)

        pygame.display.update()
if __name__ == "__main__":
    main()
