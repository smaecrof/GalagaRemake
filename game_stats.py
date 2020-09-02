# Author: Spencer Mae-Croft
# Date: 09/02/2020

class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        """ Initialize game statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()


    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit