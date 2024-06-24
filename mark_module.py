import pygame
import sys
import math
import time
import Hero_Module

projectiles = []


class Projectile:
    def __init__(self, screen, target, x, y):
        """target is cursor position at the time mouse was clicked"""
        self.screen = screen
        self.radius = 5
        self.color = ("Pink")
        self.speed = 5
        #self.x = self.screen.get_width() / 2
        #self.y = self.screen.get_height() / 2
        self.target = target
        self.x = x
        self.y = y
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
        return self.x - self.radius > self.screen.get_width() \
               or self.x + self.radius < 0 \
               or self.y - self.radius > self.screen.get_height() \
               or self.y + self.radius < 0

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
    last_fire_time = time.time()
    return last_fire_time


def main():
    pygame.init()
    pygame.display.set_caption("Mark's module")
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    clock = pygame.time.Clock()
    last_fire_time = 0

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if time.time() - last_fire_time > 0.4:
                    new_fire_time = shoot(screen)
                    last_fire_time = new_fire_time
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_ESCAPE]:
            sys.exit()

        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (0, 0, 0), (screen.get_width() / 2, screen.get_height() / 2), 10)

        for moving_projectile in projectiles:
            if moving_projectile.off_screen():
                projectiles.remove(moving_projectile)
            if moving_projectile.not_moving():
                projectiles.remove(moving_projectile)
            if not projectiles:
                pass
            else:
                moving_projectile.move()
                moving_projectile.draw()
        pygame.display.update()


if __name__ == "__main__":
    main()
