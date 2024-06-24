import pygame
import sys
import random
import time
import math
import Hero_Module
import mark_module


# need counsalur imagise (mabye as caricter salection) tj on free time
# need player charicter
# need projectile: Mark
# need enemy
# need level/location



def main():

    pygame.init()

    pygame.display.set_caption("Cool Project")

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    the_hero = Hero_Module.Hero(screen, random.randint(100,screen.get_width()-100), random.randint(100,screen.get_height()-100))
    last_fire_time = 0

    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_p]:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if time.time() - last_fire_time > 0.4:
                new_fire_time = the_hero.shoot()
                last_fire_time = new_fire_time

        pressed_keys = pygame.key.get_pressed()
        screen.fill((255, 255, 255))

        the_hero.draw()

        if pressed_keys[pygame.K_UP]:
            the_hero.y -= 5
        if pressed_keys[pygame.K_DOWN]:
            the_hero.move(0, 5)
        if pressed_keys[pygame.K_LEFT]:
            the_hero.move(-5, 0)
        if pressed_keys[pygame.K_RIGHT]:
            the_hero.move(5, 0)

        if pressed_keys[pygame.K_w]:
            the_hero.y -= 5
        if pressed_keys[pygame.K_s]:
            the_hero.move(0, 5)
        if pressed_keys[pygame.K_a]:
            the_hero.move(-5, 0)
        if pressed_keys[pygame.K_d]:
            the_hero.move(5, 0)

        #if event.type == pygame.MOUSEBUTTONDOWN:
        #    the_hero.shoot()

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

        the_hero.rotate()

        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()

main()
