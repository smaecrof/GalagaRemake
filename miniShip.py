"""
    This is a class that extends Ship and is used to 
    display smaller versions of the ship on the screen (lives)
"""

# Author: Spencer Mae-Croft
# Date: 09/04/2020

import pygame
from pygame.sprite import Sprite


class MiniShip(Sprite):
    """Creates a mini ship"""

    def __init__(self, screen):
        """Initialize a mini ship"""
        super(MiniShip, self).__init__()

        self.screen = screen
        self.image = pygame.image.load('images/miniRocket.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
