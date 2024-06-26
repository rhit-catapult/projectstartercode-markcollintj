import pygame
import sys
import random
import time
import math
import Hero_Module
import mark_module
import tj_modual

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
    width = screen.get_width()
    height = screen.get_height()
    clock2 = time.time()
    clock3 = 0
    hurt = []
    healthy = []

    harmedright = pygame.image.load("sprites/camper unhealthy right.png")
    harmedleft = pygame.image.load("sprites/camper unhealthy left.png")
    harmedup = pygame.image.load("sprites/camper unhealthy up.png")
    harmeddown = pygame.image.load("sprites/camper unhealthy down.png")
    harmedleftdown = pygame.image.load("sprites/camper unhealthy left down.png")
    harmedleftup = pygame.image.load("sprites/camper unhealthy left up.png")
    harmedrightup = pygame.image.load("sprites/camper unhealthy right up.png")
    harmedrightdown = pygame.image.load("sprites/camper unhealthy right down.png")

    unharmedright = pygame.image.load("sprites/camper healthy right.png")
    unharmedleft = pygame.image.load("sprites/camper healthy left.png")
    unharmedup = pygame.image.load("sprites/camper healthy up.png")
    unharmeddown = pygame.image.load("sprites/camper healthy down.png")
    unharmedleftdown = pygame.image.load("sprites/camper healthy left down.png")
    unharmedleftup = pygame.image.load("sprites/camper healthy left up.png")
    unharmedrightup = pygame.image.load("sprites/camper healthy right up.png")
    unharmedrightdown = pygame.image.load("sprites/camper healthy right down.png")

    pygame.mixer.music.play(-1)
    clock = pygame.time.Clock()


    while True:
        clock.tick(60)
        screen.blit(grass2, (0, 0))

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
        if pressed_keys[pygame.K_w]:
            the_hero.y -= 5
        if pressed_keys[pygame.K_s]:
            the_hero.move(0, 5)
        if pressed_keys[pygame.K_a]:
            the_hero.move(-5, 0)
        if pressed_keys[pygame.K_d]:
            the_hero.move(5, 0)
        the_hero.draw()

        if time.time() - clock3 > 3:
            if not math.floor(time.time() - clock2) % 5:
                spawns = math.floor(time.time() - clock2) / 5
                spawnernumber = int(spawns)
                waveside = random.randint(1, 4)
                if waveside == 1:
                    for i in range(0, math.floor(spawnernumber / 2)):
                        camperhealthy = tj_modual.Cammperhealthy(screen, random.randint(0, width), 0, unharmedright, unharmedleft, unharmedup, unharmeddown, unharmedleftdown, unharmedleftup, unharmedrightup, unharmedrightdown)
                        healthy.append(camperhealthy)
                        spawnernumber -= 2
                    for i in range(0, spawnernumber):
                        camperhurt = tj_modual.Cammperhurt(screen, random.randint(0, width), 0, harmedright, harmedleft,
                                                           harmedup, harmeddown, harmedleftdown, harmedleftup,
                                                           harmedrightup, harmedrightdown)
                        hurt.append(camperhurt)
                elif waveside == 2:
                    for i in range(0, math.floor(spawnernumber / 2)):
                        camperhealthy = tj_modual.Cammperhealthy(screen, random.randint(0, width), height, unharmedright, unharmedleft, unharmedup, unharmeddown, unharmedleftdown, unharmedleftup, unharmedrightup, unharmedrightdown)
                        healthy.append(camperhealthy)
                        spawnernumber -= 2
                    for i in range(0, spawnernumber):
                        camperhurt = tj_modual.Cammperhurt(screen, random.randint(0, width), height, harmedright, harmedleft, harmedup, harmeddown, harmedleftdown, harmedleftup, harmedrightup, harmedrightdown)
                        hurt.append(camperhurt)
                elif waveside == 3:
                    for i in range(0, math.floor(spawnernumber / 2)):
                        camperhealthy = tj_modual.Cammperhealthy(screen, 0, random.randint(0, height), unharmedright, unharmedleft, unharmedup, unharmeddown, unharmedleftdown, unharmedleftup, unharmedrightup, unharmedrightdown)
                        healthy.append(camperhealthy)
                        spawnernumber -= 2
                    for i in range(0, spawnernumber):
                        camperhurt = tj_modual.Cammperhurt(screen, 0, random.randint(0, height), harmedright, harmedleft, harmedup, harmeddown, harmedleftdown, harmedleftup, harmedrightup, harmedrightdown)
                        hurt.append(camperhurt)
                else:
                    for i in range(0, math.floor(spawnernumber / 2)):
                        camperhealthy = tj_modual.Cammperhealthy(screen, width, random.randint(0, height), unharmedright, unharmedleft, unharmedup, unharmeddown, unharmedleftdown, unharmedleftup, unharmedrightup, unharmedrightdown)
                        healthy.append(camperhealthy)
                        spawnernumber -= 2
                    for i in range(0, spawnernumber):
                        camperhurt = tj_modual.Cammperhurt(screen, width, random.randint(0, height), harmedright, harmedleft, harmedup, harmeddown, harmedleftdown, harmedleftup, harmedrightup, harmedrightdown)
                        hurt.append(camperhurt)
                clock3 = time.time()
        camperstoremovehurt = []
        for Camperhurt in hurt:
            for bullet in the_hero.bullets:
                if Camperhurt.hitby(bullet, the_hero.x, the_hero.y):
                    if Camperhurt not in camperstoremovehurt:
                        camperstoremovehurt.append(Camperhurt)
                        the_hero.bullets.remove(bullet)
            Camperhurt.move(the_hero.x, the_hero.y)
            Camperhurt.draw(the_hero.x, the_hero.y)
        for Camperhurt in camperstoremovehurt:
            hurt.remove(Camperhurt)
        camperstoremovehealthy = []
        for camperhealthy in healthy:
            for bullet in the_hero.bullets:
                if camperhealthy.hitby(bullet, the_hero.x,the_hero.y):
                    if camperhealthy not in camperstoremovehealthy:
                        camperstoremovehealthy.append(camperhealthy)
                        camperhurt = tj_modual.Cammperhurt(screen, camperhealthy.x, camperhealthy.y, harmedright,
                                                           harmedleft, harmedup, harmeddown, harmedleftdown,
                                                           harmedleftup, harmedrightup, harmedrightdown)
                        hurt.append(camperhurt)
                        the_hero.bullets.remove(bullet)
            camperhealthy.move(the_hero.x, the_hero.y)
            camperhealthy.draw(the_hero.x, the_hero.y)
        for camperhealthy in camperstoremovehealthy:
            healthy.remove(camperhealthy)


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
        pygame.display.update()

if __name__ == "__main__":
    main()