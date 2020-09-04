"""
   This is the alien class which stores the information and
   functionality needed to draw an alien on the screen
"""

# Author: Spencer Mae-Croft
# Date: 09/01/2020

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in an alien fleet"""
    def __init__(self, ai_settings, screen):
        """Initialize an alien and set its starting position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/ufo.png')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact location/position
        self.x_coord = float(self.rect.x)

    def update(self, stats):
        """Move the alien right or left."""
        if stats.game_active:
            self.x_coord += (self.ai_settings.alien_speed_factor *
                       self.ai_settings.fleet_direction)
            self.rect.x = self.x_coord

    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()

        return self.rect.right >= screen_rect.right or self.rect.left <= 0
