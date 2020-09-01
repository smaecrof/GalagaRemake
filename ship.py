# Author: Spencer Mae-Croft
# Date: 09/01/2020

import pygame 

class Ship():

    def __init__(self, ai_settings,  screen):
        """Initialize a ship and set its starting position"""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect. 
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom of the screen (centered) 
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Movement flag 
        self.moving_right = False
        self.moving_left = False
    
        # Buffers for ship object 
        self.windowSize = pygame.display.get_window_size()
        self.rightBuffer = self.windowSize[0] - 32
        self.leftBuffer = 32

            

    def update(self):
        """Update the ship's position based on the movement flag"""
        if self.moving_right and self.rect.centerx <= self.rightBuffer:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.centerx >= self.leftBuffer:
            self.rect.centerx -= self.ai_settings.ship_speed_factor

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)


