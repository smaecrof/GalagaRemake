"""
    Creates a ship object and stores location of ship
"""

# Author: Spencer Mae-Croft
# Date: 09/01/2020

import pygame


class Ship():
    """Creates a ship object"""

    def __init__(self, ai_settings,  screen):
        """Initialize a ship and set its starting position"""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/rocketship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom of the screen (centered)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for a ship's center
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

        # Buffers for ship object
        self.window_size = pygame.display.get_window_size()
        self.right_buffer = self.window_size[0] - 32
        self.left_buffer = 32

    def update(self):
        """Update the ship's position based on the movement flag"""
        if self.moving_right and self.rect.centerx <= self.right_buffer:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.centerx >= self.left_buffer:
            self.rect.centerx -= self.ai_settings.ship_speed_factor

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship after a collision"""
        self.center = self.screen_rect.centerx
