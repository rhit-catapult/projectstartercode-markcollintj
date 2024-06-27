import pygame
import sys
import random
import time
import math
import Hero_Module
import mark_module
import opening_screen
import tj_modual

# need enemy



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
    pygame.mixer.music.set_volume(.5)
    clock = pygame.time.Clock()
    pfp = opening_screen.Menu(screen)
    char_pfp = 0
    width = screen.get_width()
    height = screen.get_height()
    clock2 = time.time()
    clock3 = 0
    hurt = []
    healthy = []
    score = 0
    font1 = pygame.font.SysFont("impact", 20)
    #caption1 = font1.render(score , True, pygame.Color("White"))
    player_hp = 0

    bar_list = [
        "sprites/health_bar.png",
        "sprites/3hp.png",
        "sprites/2hp.png",
        "sprites/1hp.png",
        "sprites/Game_Over.png",

    ]

    # bar = pygame.image.load(bar_list[player_hp ])

    gasshole = [
        "grasshole/aaron.mp3",
        "grasshole/kali.mp3",
        "grasshole/ruby.mp3",
        "grasshole/ethan.mp3",
        "grasshole/eli.mp3",
        "grasshole/michal.mp3",
        "grasshole/hoit.mp3",
        "grasshole/reed.mp3",
        "grasshole/braydon.mp3",
        "grasshole/clare.mp3",
        "grasshole/elly.mp3",
        "grasshole/emmet.mp3",
        "grasshole/fox.mp3",
        "grasshole/sparky.mp3",
        "grasshole/tyler.mp3",
    ]


    #grasshole_sound = pygame.mixer.Sound(gasshole[char_pfp % 15])

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

        # while player_hp >= 4:
        #     print(player_hp)

        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_p]:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if time.time() - last_fire_time > 0.2:
                    new_fire_time = the_hero.shoot()
                    last_fire_time = new_fire_time

        screen.fill((255,255,255))
        pressed_keys = pygame.key.get_pressed()
        screen.blit(grass2, (0,0))


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
        caption1 = font1.render(f"{score}", True, pygame.Color("White"))

        grasshole_sound = pygame.mixer.Sound(gasshole[char_pfp % 15])
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
                        pygame.mixer.Sound.play(grasshole_sound)
                        score += 100
                        player_hp += 1
                        camperstoremovehurt.append(Camperhurt)
                        the_hero.bullets.remove(bullet)


            Camperhurt.move(the_hero.x, the_hero.y)
            Camperhurt.draw(the_hero.x, the_hero.y)
            # hero_hit_box2 = pygame.Rect(the_hero.x, the_hero.y, the_hero.image.get_width(), the_hero.image.get_height())

            # if Camperhurt.hitby(the_hero, the_hero.x, the_hero.y):
            #     player_hp += 1

        for Camperhurt in camperstoremovehurt:
            hurt.remove(Camperhurt)
        camperstoremovehealthy = []
        for camperhealthy in healthy:
            for bullet in the_hero.bullets:
                if camperhealthy.hitby(bullet, the_hero.x,the_hero.y):
                    if camperhealthy not in camperstoremovehealthy:
                        #pygame.mixer.Sound.play(grasshole_sound)
                        camperstoremovehealthy.append(camperhealthy)
                        camperhurt = tj_modual.Cammperhurt(screen, camperhealthy.center_x, camperhealthy.center_y, harmedright,
                                                           harmedleft, harmedup, harmeddown, harmedleftdown,
                                                           harmedleftup, harmedrightup, harmedrightdown)

                        hurt.append(camperhurt)
                        the_hero.bullets.remove(bullet)

            if camperhealthy.hitby(the_hero, the_hero.x, the_hero.y):
                    player_hp += 1

            camperhealthy.move(the_hero.x, the_hero.y)
            camperhealthy.draw(the_hero.x, the_hero.y)
            # if the_hero.hit_by2(camperhealthy.hit_box):
            #     player_hp += 1
        for camperhealthy in camperstoremovehealthy:
            healthy.remove(camperhealthy)

        #pfp.play_sound(char_pfp)

        # for camperhealthy in healthy:
        #     if camperhealthy.hitby(the_hero, the_hero.x, the_hero.y):
        #         player_hp += 1

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
        pfp.draw_pfp(char_pfp % 15)
        #screen.blit(bar, (0, 0))
        screen.blit(caption1, (140,30))
        the_hero.rotate()

        #bar = pygame.image.load(bar_list[player_hp])

        bar = pygame.image.load(bar_list[player_hp])

        screen.blit(bar, (0, 0))
        # don't forget the update, otherwise nothing will show up!


        while player_hp >= 4:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[pygame.K_p]:
                    sys.exit()
            screen.fill((0,0,0))
            yes = pygame.image.load("sprites/Game_Over.png")
            screen.blit(yes, (screen.get_width() // 2 - 250, screen.get_height() // 2 - 250))
            pygame.display.update()
        pygame.display.update()







main()
