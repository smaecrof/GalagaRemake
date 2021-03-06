"""
    Stores functionality to store stats and also to reset score after game
    has ended
"""

# Author: Spencer Mae-Croft
# Date: 09/02/2020


class GameStats():
    """Track statistics for Alien Invasion."""
    def __init__(self, ai_settings):
        """ Initialize game statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # High Score
        self.high_score = 0

        # Start Alien Invasion in an active state
        self.game_active = True

        # Start game in an inactive state
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
