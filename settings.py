# Author: Spencer Mae-Croft
# Date: 09/01/2020

class Settings():
    """A class to store all settings for Galaga"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen Settings 
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (0,0,0)

        # Ship settings
        self.ship_speed_factor = 5
        self.ship_limit = 3

        # Bullet settings 
        self.bullet_speed_factor = 6
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        # Alien Settings 
        self.alien_speed_factor = 3 
        self.fleet_drop_speed = 10

        # fleet_direction of 1 represents right, -1 represents left
        self.fleet_direction = 1
