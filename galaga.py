# Author: Spencer Mae-Croft 
# Date: 08/31/2020

import sys 
import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group

def run_game():
    # Initialize pygame, settings, and screen object  
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Galaga")


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
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()

        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
                        


run_game()

