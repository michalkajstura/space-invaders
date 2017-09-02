import pygame


class Ship():

    def __init__(self, settings, screen):
        """Initialize ship and set its starting position"""
        self.screen = screen

        #ship's velocity
        self.settings = settings

        # loads the image and creates rectangle 
        self.image = pygame.image.load("images/ship.png")
        self.image = pygame.transform.scale(self.image, (settings.ship_size, settings.ship_size))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # starts ship at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Movement flags
        self.moving_right = False
        self.moving_left = False

        self.center = float(self.rect.centerx)

    def blit_me(self):
        """Draws the shit at its current location"""
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        """Update the ship's positon based on movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.velocity
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.settings.velocity

        # Update rect object from self.center
        self.rect.centerx = self.center


