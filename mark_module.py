import pygame
import sys
import math
import Hero_Module
import tj_modual

projectiles = []

class Projectile:
    def __init__(self, screen, target):
        """target is cursor position at the time mouse was clicked"""
        self.screen = screen
        self.radius = 5
        self.color = (128, 128, 128)
        self.speed = 5
        self.x = 300
        self.y = 300
        self.target = target
        # self.x = Hero.x
        # self.y = Hero.y
        self.delta_x = target[0] - self.x
        self.delta_y = target[1] - self.y
        self.q = math.atan2(self.delta_y, self.delta_x)
        self.small_delta_x = math.cos(self.q) * self.speed
        self.small_delta_y = math.sin(self.q) * self.speed
        self.hit_box = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.small_delta_x
        self.y += self.small_delta_y

    def off_screen(self):
        return self.x - self.radius > self.screen.get_width() or self.x + self.radius < 0 or self.y - self.radius > self.screen.get_height() or self.y + self.radius < 0

    def not_moving(self):
        check_x = self.delta_x == 0
        check_y = self.delta_y == 0
        return check_x and check_y

    def hits(self, camperhealthy, camperhurt):
        if self.hit_box.colliderect(camperhurt.hit_box):
            projectiles.remove(self)
        if self.hit_box.colliderect(camperhealthy.hit_box):
            projectiles.remove(self)

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
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_ESCAPE]:
            sys.exit()
        if pressed_keys[pygame.K_p]:
            for moving_projectiles in projectiles:
                print(moving_projectiles.small_delta_x, moving_projectiles.small_delta_y)
            # TODO: Add you events code

        # TODO: Fill the screen with whatever background color you like!
        screen.fill((255, 255, 255))

        # TODO: Add your project code
        for moving_projectile in projectiles:
            if moving_projectile.off_screen():
                projectiles.remove(moving_projectile)
            if moving_projectile.not_moving():
                projectiles.remove(moving_projectile)
            if projectiles == []:
                pass
            else:
                moving_projectile.move()
                moving_projectile.draw()
        print(len(projectiles))
        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()

if __name__ == "__main__":
    main()