"""
    Stores easy to access game settings. Pylint would like me to end this settings file
    so that there are less instance variables. Not sure if I'll do this yet but I see where
    the point could be made that this file won't scale well with the game.
"""

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
        self.bg_color = (15, 15, 15)
        self.bg_image = pygame.image.load("images/space_bg.jpeg")


        # Ship settings
        self.ship_limit = 3
        
        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (252, 40, 3)
        self.bullets_allowed = 3

        # Alien Settings 
        self.alien_speed_factor = 6

        # Alien Settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed_factor = 5
        self.bullet_speed_factor = 8
        self.alien_speed_factor = 3

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings."""
        if self.ship_speed_factor < 8:
            self.ship_speed_factor *= self.speedup_scale

        if self.bullet_speed_factor < 8:
            self.bullet_speed_factor *= self.speedup_scale

        self.fleet_drop_speed *= self.speedup_scale
