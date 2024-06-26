import pygame
import sys

class Menu:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.x = screen.get_width() // 2 - 250
        self.y = screen.get_height() // 2 - 250
        self.councelor = ["Aaron", "Kali", "Ruby", "Ethan", "Eli", "Michael", "Hoyt", "Reid","Brayden","Claire","Elly","Emmett","Fox","Sparky","Tyler"]
        self.displayed_character = 0
        self.images = [
            "sprites/Cliped_aaron.png",
            "sprites/cliped_Kali.png",
            "sprites/cliped_ruby.png",
            "sprites/Cliped_Ethan.png",
            "sprites/Cliped_Eli.png",
            "sprites/Micheal_cliped.png",
            "sprites/cliped_HOYT.png",
            "sprites/Cliped_Reid.png",
            "sprites/clipped_brayden.png",
            "sprites/clipped_clair.png",
            "sprites/clipped_elly.png",
            "sprites/clipped_emmett.png",
            "sprites/clipped_fox.png",
            "sprites/clipped_sparky.png",
            "sprites/clipped_tyler.png"
        ]

        self.char_png = pygame.image.load(self.images[self.displayed_character])

        self.Menu1 = pygame.image.load("sprites/Menu.png")

    def draw(self):
        self.screen.blit(self.Menu1, (self.x, self.y))

    def Char_select(self, h):
        self.displayed_character = (self.displayed_character + h) % len(self.councelor)
        # print(self.councelor[self.displayed_character])

    def character_selected(self):
        self.char_png = pygame.image.load(self.images[self.displayed_character])
        font1 = pygame.font.SysFont("impact", 40)
        caption1 = font1.render(self.councelor[self.displayed_character], True, pygame.Color("Black"))
        self.screen.blit(caption1, (self.x + 225, self.y + 200))
    def draw_character(self):
        self.screen.blit(self.char_png, (self.x + 200, self.y + 250))

    def draw_pfp(self, x):
        pfp_img = [
            "sprites/pfp_aaron.png",
            "sprites/pfp_kali.png",
            "sprites/pfp_ruby.png",
            "sprites/pfp_ethan.png",
            "sprites/pfp_eli.png",
            "sprites/pfp_micheal.png",
            "sprites/pfp_hoyt.png",
            "sprites/pfp_reid.png",
            "sprites/pfp_brayden.png",
            "sprites/png_claire.png",
            "sprites/pfp_elly.png",
            "sprites/pfp_emmet.png",
            "sprites/pfp_fox.png",
            "sprites/pfp_sparky.png",
            "sprites/pfp_tyler.png",
        ]

        pfp_png = pygame.image.load(pfp_img[x])

        self.screen.blit(pfp_png, (0, 0))

    # def play_sound(self,x):
    #
    #     gasshole_sound = [
    #         "grasshole/aaron.mp3",
    #         "grasshole/kali.mp3",
    #         "grasshole/ruby.mp3",
    #         "grasshole/ethan.mp3",
    #         "grasshole/eli.mp3",
    #         "grasshole/michal.mp3",
    #         "grasshole/hoit.mp3",
    #         "grasshole/reed.mp3",
    #         "grasshole/braydon.mp3",
    #         "grasshole/clare.mp3",
    #         "grasshole/elly.mp3",
    #         "grasshole/emmet.mp3",
    #         "grasshole/fox.mp3",
    #         "grasshole/sparky.mp3",
    #         "grasshole/tyler.mp3",
    #     ]
    #
    #     #grasshole_sound = pygame.mixer.Sound(gasshole_sound[self.displayed_character % 15])
    #
    #     grasshole_sound = pygame.mixer.Sound(gasshole_sound[x % 15])
    #
    #     pygame.mixer.Sound(grasshole_sound)
# pygame.init()
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# clock = pygame.time.Clock()
# Menu1 = pygame.image.load("sprites/Menu.png")
# menu = Menu(screen)
#                           pygame.mixer.Sound(gasshole[char_pfp % 15])
# font1 = pygame.font.SysFont("impact",40)
# menu_state = 0
# while True:
#     clock.tick(60)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#         # if event.type == pygame.KEYDOWN:
#         #     pressed_keys = pygame.key.get_pressed()
#         #     if pressed_keys[pygame.K_RIGHT]:
#         #         menu.Char_select(1)
#         #     if pressed_keys[pygame.K_LEFT]:
#         #         menu.Char_select(-1)
#
#     pressed_keys = pygame.key.get_pressed()
#     if pressed_keys[pygame.K_p]:
#         sys.exit()
#
#     # menu.draw()
#     # menu.character_selected()
#     # menu.draw_character()
#     #
#     # pygame.display.update()
#
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.KEYDOWN:
#                 pressed_keys = pygame.key.get_pressed()
#                 if pressed_keys[pygame.K_RIGHT]:
#                     menu.Char_select(1)
#                 if pressed_keys[pygame.K_LEFT]:
#                     menu.Char_select(-1)
#
#         pressed_keys = pygame.key.get_pressed()
#         if pressed_keys[pygame.K_p]:
#             sys.exit()
#
#         menu.draw()
#         menu.character_selected()
#         menu.draw_character()
#
#         pygame.display.update()
#
#
#         if pressed_keys [pygame.K_RETURN]:
#             print("menu closed")
#             break