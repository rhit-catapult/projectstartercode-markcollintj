import pygame
import sys
import random
import time
import mark_module

class Menu:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.x = screen.get_width()/2-250
        self.y = screen.get_height()/2-250
        self.councelor = ["AAron","Kali","Ruby","Ethan","Eli","Michael","Hoyt","Reid"]
        self.displayed_character = 0
        self.char = self.councelor[0]
        self.char_png = "sprites/wrong.png"
        self.image = pygame.image.load(self.char_png)
    def draw(self):
        screen.blit(Menu1, (self.x, self.y))


    def Char_select(self,h):

        self.displayed_character += h
        self.char = self.displayed_character
        print(self.char)

    def character_selected(self):
        if self.char == 0:
            self.char_png = "sprites/Cliped_aaron"
        if self.char == 1:
            self.char_png = "sprites/cliped_Kali"
        if self.char == 2:
            self.char_png = "sprites/cliped_ruby"
        if self.char == 3:
            self.char_png = "sprites/Cliped_Ethan"
        if self.char == 4:
            self.char_png = "sprites/Cliped_Eli"
        if self.char == 5:
            self.char_png = "sprites/Micheal_cliped"
        if self.char == 6:
            self.char_png = "sprites/cliped_HOYT"
        if self.char == 7:
            self.char_png = "sprites/Cliped_Reid"

    def draw_character(self):
        #character2 = pygame.image.load(self.char_png)
        screen.blit(self.image, (self.x + 200, self.y + 250))



pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
font1 = pygame.font.SysFont("[pmingliuextb]",70)

Menu1 = pygame.image.load("sprites/Menu.png")
menu = Menu(screen)

#character2 = pygame.image.load(Menu.char_png)

#caption1 = font1.render("The Grasshole Apocolapse", True, (23, 13, 163))

while True:

        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[pygame.K_RIGHT]:
                    menu.Char_select(1)
                if pressed_keys[pygame.K_LEFT]:
                    menu.Char_select(-1)



        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_p]:
            sys.exit()


        #screen.blit(Menu1, (screen.get_width()/2-250, screen.get_height()/2-250))

        menu.draw()

        menu.character_selected()
        menu.draw_character()


        pygame.display.update()

main()