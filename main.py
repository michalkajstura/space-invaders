import pygame
import functions as f
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from alien import Alien

settings = Settings()

screen = pygame.display.set_mode(
    (settings.screen_width, settings.screen_height))
pygame.display.set_caption('Alien Invasion')
# background= pygame.image.load('images/tlo.png')
# background = pygame.transform.scale(background, (settings.screen_width, settings.screen_height))
settings.background = f.make_random_background(settings)

clock = pygame.time.Clock()
crashed = False

# make a ship
ship = Ship(settings, screen)

# make groups
bullets = Group()
alien_bullets = Group()
aliens = Group()


# time to fire a bullet by alien [s]
i = 60 * 1

while not f.check_lose(settings, aliens):
    f.check_events(settings, screen, ship, bullets)
    ship.update()
    f.update_bullets(bullets, alien_bullets)
    f.update_fleet(settings, screen, aliens)
    f.check_collisions(bullets, aliens, ship, alien_bullets)
    f.update_screen(settings, screen, ship, bullets, alien_bullets, aliens)
    clock.tick(60)
    f.check_win(settings, screen, aliens, clock)

    i -= 1
    if i < 0:
        i = 60 * settings.shooting_time
        f.shoot(settings, screen, aliens, alien_bullets)
