# Author: Spencer Mae-Croft
# Date: 09/01/2020

import pygame

class Settings():
    """A class to store all settings for Galaga"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen Settings 
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (0,0,0)
        self.bg_image = pygame.image.load("images/space_bg.jpeg")

        # Ship settings
        self.ship_limit = 3

        # Bullet settings 
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (252,40,3)
        self.bullets_allowed = 3

        # Alien Settings 
        self.fleet_drop_speed = 10


        # How quickly the game speeds up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed_factor = 5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 3

        # fleet_direction of 1 represents right; -1 represents left 
        self.fleet_direction = 1

    

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

