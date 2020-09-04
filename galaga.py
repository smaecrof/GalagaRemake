"""
    Beginning of the game, main game loop
"""

# Author: Spencer Mae-Croft # Date: 08/31/2020
# Date: 08/31/2020

import pygame
from pygame.sprite import Group
import game_functions as gf
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    """The main program loop, creation of screen elements"""

    # Initialize pygame, settings, and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                     ai_settings.screen_height))
    pygame.display.set_caption("Galaga")
<<<<<<< HEAD
    
=======

    # Make a Play button
    play_button = Button(screen, "Play")

>>>>>>> nGraphics
    # Create an instance to store game statistics
    stats = GameStats(ai_settings)

    # Make a Ship
    ship = Ship(ai_settings, screen)

    # Make a group of bullets and a group of aliens
    bullets = Group()
    aliens = Group()

    # Creating an enemy fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game
    while True:
<<<<<<< HEAD
        # Checking for keyboard events  
<<<<<<< HEAD
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()

            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen,  ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
=======
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
=======
>>>>>>> nGraphics

        # Checking for keyboard events
        gf.check_events(ai_settings, screen, stats,
                        play_button, ship, aliens, bullets)

        # Create scoreboard
        scoreboard = Scoreboard(ai_settings, screen, stats)

        # Update group objects
        ship.update()
        bullets.update()

        gf.update_bullets(ai_settings, screen, stats,
                          scoreboard, ship, aliens, bullets)
        gf.update_aliens(ai_settings, stats, screen,  ship, aliens, bullets)
<<<<<<< HEAD
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)
>>>>>>> nGraphics
                        
=======
        gf.update_screen(ai_settings, screen, stats,
                         scoreboard, ship, aliens, bullets, play_button)
>>>>>>> nGraphics


run_game()
