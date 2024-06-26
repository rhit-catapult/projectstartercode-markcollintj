import pygame
import sys
import random
import time
import math
import mark_module
import Hero_Module


class Power_up:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.x = random.randint(100,screen.get_width()-100)
        self.y = random.randint(100,screen.get_height()-100)
        self.image = pygame.image.load("sprites/shoe_bag_power-up.png")
        self.hit_box = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def find_place(self):
        self.x = random.randint(100, self.screen.get_width() - 100)
        self.y = random.randint(100, self.screen.get_height() - 100)
    def hit_move(self):
        self.hit_box = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    # def colleccted(self, hero):
     #
     #     if self.hit_box.colliderect(hero.hit_box):
     #         hero.remove(self)
     #



clock3 = time.time()



def main():

    pygame.init()


    pygame.display.set_caption("Hero module")

    screen = pygame.display.set_mode((640, 480))
    pressed_keys = pygame.key.get_pressed()
    clock = pygame.time.Clock()
    clock2 = time.time()
    the_hero = Hero_Module.Hero(screen, random.randint(100,screen.get_width()-100), random.randint(100,screen.get_height()-100))
    power_up = Power_up(screen)
    n = 0
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                the_hero.shoot()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    power_up.find_place()
            if pressed_keys[pygame.K_p]:
                sys.exit()


        screen.fill((0, 0, 0))
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_h]:
            the_hero.rotate()


        the_hero.draw()

        print(clock2)


        if pressed_keys[pygame.K_w]:
            the_hero.y -= 5
        if pressed_keys[pygame.K_s]:
            the_hero.move(0, 5)
        if pressed_keys[pygame.K_a]:
            the_hero.move(-5, 0)
        if pressed_keys[pygame.K_d]:
            the_hero.move(5, 0)



        for moving_projectile in the_hero.bullets:
            if moving_projectile.off_screen():
                the_hero.bullets.remove(moving_projectile)
            if moving_projectile.not_moving():
                the_hero.bullets.remove(moving_projectile)
            if not the_hero.bullets:
                pass
            else:
                moving_projectile.move()
                moving_projectile.draw()


        if the_hero.hit_by(power_up):
            power_up.find_place()

        the_hero.rotate()
        power_up.draw()
        power_up.hit_move()


        power_up.draw()
        power_up.hit_move()



        pygame.display.update()
if __name__ == "__main__":
    main()
