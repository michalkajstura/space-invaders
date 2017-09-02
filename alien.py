import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Spawn aliens and control their behaviour"""
    def __init__(self, settings, screen):
        super().__init__()
        self.screen = screen
        self.settings = settings
        
        # load the image of alien and get its rectangle 
        self.image = pygame.image.load('images/alien.png')
        self.image = pygame.transform.scale(self.image, (settings.alien_size, settings.alien_size))
        self.rect = self.image.get_rect()

        # Spawn each new alien near top left 
        self.rect.x = settings.alien_size
        self.rect.y = self.rect.height

        # Store exact position
        self.x = float(self.rect.x)

        # moving direction
        self.moving_direction = 'RIGHT'

    def blit_me(self):
        """Blits alien at its current position"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Updates alien fleet postion"""
        self.x -= self.settings.alien_velocity
        self.rect.x = self.x






