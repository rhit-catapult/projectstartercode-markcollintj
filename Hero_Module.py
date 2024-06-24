import pygame
import sys
import random
import time
import math
import mark_module


#class Bullet:
    #def __init__(self, screen: pygame.surface, x, y):
        #self.screen = screen
        #self.x = x
       # self.y = y
       # self.speed = 10
   # def move(self):
   #     """ Move the self.y value of the Raindrop down the screen (y increase) at the self.speed. """
  #      self.y -= self.speed
 #   def draw(self):
 #     pygame.draw.line(self.screen, "Green",(self.x, self.y),(self.x, self.y + 5) )
#



class Hero:
    def __init__(self, screen: pygame.Surface,x , y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speedx = 5
        self.speedy = 5
        self.image = pygame.image.load("Counselor.png")
        self.bullets = []
        self.angle = 0
        self.mouse_pos = pygame.mouse.get_pos()
    def move(self, xa, ya):

        self.y += ya
        self.x += xa



    def draw(self):

        rotated_image = pygame.transform.rotate(self.image, self.angle)

        self.screen.blit(rotated_image, (self.x, self.y))

    def rotate(self):
        dx = pygame.mouse.get_pos()[0] - (self.x + self.image.get_width() / 2)
        dy = pygame.mouse.get_pos()[1] - (self.y + self.image.get_height() / 2)

        self.angle = math.degrees(math.atan2(-dy, dx)) - 90



    def shoot(self):
        new_bullet = mark_module.Projectile(self.screen,pygame.mouse.get_pos())
        self.bullets.append(new_bullet)


    def hit_by(self, camper):

        hero_hit_box = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        return hero_hit_box.collidepoint(camper.x,camper.y)

class barrier:
    def __init__(self, screen: pygame.Surface, x, y):

        self.screen = screen
        self.x = x
        self.y = y


    #def collide_check(self):







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

        Projectile.x =


        screen.fill((0, 0, 0))
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_h]:
            heros.rotate()


        heros.draw()

        if pressed_keys[pygame.K_UP]:
            heros.y -= 5
        if pressed_keys[pygame.K_DOWN]:
            heros.move(0, 5)
        if pressed_keys[pygame.K_LEFT]:
            heros.move(-5, 0)
        if pressed_keys[pygame.K_RIGHT]:
            heros.move(5, 0)


        if pressed_keys[pygame.K_w]:
            heros.y -= 5
        if pressed_keys[pygame.K_s]:
            heros.move(0, 5)
        if pressed_keys[pygame.K_a]:
            heros.move(-5, 0)
        if pressed_keys[pygame.K_d]:
            heros.move(5, 0)

        if event.type == pygame.MOUSEBUTTONDOWN:
            heros.shoot()

        for moving_projectile in heros.bullets:
            if moving_projectile.off_screen():
                heros.bullets.remove(moving_projectile)
            if moving_projectile.not_moving():
                heros.bullets.remove(moving_projectile)
            if not heros.bullets:
                pass
            else:
                moving_projectile.move()
                moving_projectile.draw()

        heros.rotate()


        pygame.display.update()
if __name__ == "__main__":
    main()
