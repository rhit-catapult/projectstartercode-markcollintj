import pygame
import sys
import math

projectiles = []

class Projectile:
    def __init__(self, screen, target):
        """target is cursor position at the time mouse was clicked"""
        self.screen = screen
        self.radius = 5
        self.color = (128, 128, 128)
        self.speed = 5
        self.x = 20
        self.y = 20
        self.target = target
        # self.x = Hero.x
        # self.y = Hero.y
        self.delta_x = self.x - target[0]
        self.delta_y = self.y - target[1]
        self.q = math.atan(self.delta_y / self.delta_x)
        self.small_delta_x = self.speed * math.cos(self.q)
        self.small_delta_y = self.speed * math.sin(self.q)

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.small_delta_x
        self.y += self.small_delta_y
    def off_screen(self):
        return self.x - self.radius > self.screen.get_width() or self.x + self.radius < 0 or self.y - self.radius > self.screen.get_height() or self.y + self.radius < 0

def shoot(screen):
    projectile = Projectile(screen, pygame.mouse.get_pos())
    projectiles.append(projectile)
def main():
    # turn on pygame
    pygame.init()

    # create a screen
    pygame.display.set_caption("Mark's module")
    # TODO: Change the size of the screen as you see fit!
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    # let's set the framerate
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                shoot(screen)
            if event.type == pygame.K_ESCAPE:
                sys.exit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_ESCAPE]:
            sys.exit()
            # TODO: Add you events code

        # TODO: Fill the screen with whatever background color you like!
        screen.fill((255, 255, 255))

        # TODO: Add your project code
        for moving_projectile in projectiles:
            moving_projectile.move()
            moving_projectile.draw()
            if moving_projectile.off_screen():
                projectiles.remove(moving_projectile)
        print(len(projectiles))
        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()

if __name__ == "__main__":
    main()