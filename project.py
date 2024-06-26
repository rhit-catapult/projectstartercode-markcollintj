import pygame
import sys
import random
import time
import math
import Hero_Module
import mark_module
import opening_screen

# need counsalur imagise (mabye as caricter salection) tj on free time
# need player charicter
# need projectile: Mark
# need enemy
# need level/location



def main():

    pygame.init()
    # unharmed_right = pygame.image.load("sprites/camper healthy right.png")
    # unharmed_left = pygame.image.load("sprites/camper healthy left.png")
    # unharmed_up = pygame.image.load("sprites/camper healthy up.png")
    pygame.mixer.music.load("spook4.mp3")
    grass = pygame.image.load("grass.png")
    pygame.display.set_caption("Cool Project")
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    grass2 = pygame.transform.scale(grass, (screen.get_width(), screen.get_height()))
    the_hero = Hero_Module.Hero(screen, random.randint(100,screen.get_width()-100), random.randint(100,screen.get_height()-100))
    last_fire_time = 0
    Menu1 = pygame.image.load("sprites/Menu.png")
    menu = opening_screen.Menu(screen)
    menu_state = True
    pygame.mixer.music.play(-1)
    clock = pygame.time.Clock()
    bar = pygame.image.load("sprites/health_bar.png")
    pfp = opening_screen.Menu(screen)
    char_pfp = 0
    while True:

        while menu_state:
            clock.tick(60)

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        menu.Char_select(1)
                        char_pfp += 1
                    if event.key == pygame.K_LEFT:
                        menu.Char_select(-1)
                        char_pfp -= 1
                    if event.key == pygame.K_RETURN:
                        print("Menu closed")
                        menu_state = False



            menu.draw()
            menu.character_selected()
            menu.draw_character()
            pygame.display.update()



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

        screen.fill((255,255,255))
        pressed_keys = pygame.key.get_pressed()
        screen.blit(grass2, (0,0))
        pfp.draw_pfp(char_pfp)
        screen.blit(bar, (0, 0))

        the_hero.draw()

        # if pressed_keys[pygame.K_UP]:
        #     the_hero.y -= 5
        # if pressed_keys[pygame.K_DOWN]:
        #     the_hero.move(0, 5)
        # if pressed_keys[pygame.K_LEFT]:
        #     the_hero.move(-5, 0)
        # if pressed_keys[pygame.K_RIGHT]:
        #     the_hero.move(5, 0)

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
        screen.blit(bar, (0, 0))
        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()







main()
