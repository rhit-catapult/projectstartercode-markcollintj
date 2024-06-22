import pygame
import sys
import random
import time



class Bullet:
    def __init__(self, screen: pygame.surface, x, y):
        """ Creates a Raindrop sprite that travels down at a random speed. """
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = 10
    def move(self):
        """ Move the self.y value of the Raindrop down the screen (y increase) at the self.speed. """
        self.y -= self.speed
    def draw(self):
      pygame.draw.line(self.screen, "Green",(self.x, self.y),(self.x, self.y + 5) )




class Hero:
    def __init__(self, screen: pygame.Surface,x , y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speedx = 5
        self.speedy = 5
        self.raidius = 20
        self.color = pygame.Color("Blue")
        self.bullets = []
    def move(self, xa, ya):

        self.y += ya
        self.x += xa


    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.raidius)

    def shoot(self):
        new_bullet = Bullet(self.screen,self.x,self.y)
        self.bullets.append(new_bullet)

def main():

    pygame.init()


    pygame.display.set_caption("Hero module")

    screen = pygame.display.set_mode((640, 480))
    #pressed_keys = pygame.key.get_pressed()
    clock = pygame.time.Clock()

    heros = Hero(screen, random.randint(100,screen.get_width()-100), random.randint(100,screen.get_height()-100))

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                heros.shoot()
                print("you shot")

            # TODO: Add you events code

        screen.fill((0, 0, 0))

        heros.draw()

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            heros.y -= 5
            #print("h8")
        if pressed_keys[pygame.K_DOWN]:
            heros.move(0, 5)
        if pressed_keys[pygame.K_LEFT]:
            heros.move(-5, 0)
        if pressed_keys[pygame.K_RIGHT]:
            heros.move(5, 0)


        for Bullet in heros.bullets:
            Bullet.move()
            Bullet.draw()




        pygame.display.update()
if __name__ == "__main__":
    main()
