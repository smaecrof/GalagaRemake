# Author: Spencer Mae-Croft # Date: 08/31/2020
# Date: 08/31/2020

import sys
import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # Initialize pygame, settings, and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                     ai_settings.screen_height))
    pygame.display.set_caption("Galaga")

    # Make a Play button
    play_button = Button(ai_settings, screen, "Play")

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

        # Checking for keyboard events
        gf.check_events(ai_settings, screen, stats,
                        play_button, ship, aliens, bullets)

        # Create scoreboard
        sb = Scoreboard(ai_settings, screen, stats)

        # Update group objects
        ship.update()
        bullets.update()

        gf.update_bullets(ai_settings, screen, stats,
                          sb, ship, aliens, bullets)
        gf.update_aliens(ai_settings, stats, screen,  ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats,
                         sb, ship, aliens, bullets, play_button)


run_game()
