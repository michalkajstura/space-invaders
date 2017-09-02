import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""
    def __init__(self, settings, screen, ship):
        super().__init__()
        self.screen = screen

        # Create bullet
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullets posstion in decimal value
        self.y = float(self.rect.y)

        self.color = settings.bullet_color
        self.velocity = settings.bullet_velocity

    def update(self):
        """Move the bullet up"""
        self.y -= self.velocity
        self.rect.y = self.y
    
    def draw_bullet(self):
        """Draw the bullet at its current possition"""
        pygame.draw.rect(self.screen, self.color, self.rect)


class AlienBullet(Bullet):
    """A class to manage bullets from alien fleet"""

    def __init__(self, settings, screen, ship):
        super().__init__(settings, screen, ship)
        self.color = settings.alien_bullet_color

    def update(self):
        """Move the bullet down"""
        self.y += self.velocity
        self.rect.y = self.y