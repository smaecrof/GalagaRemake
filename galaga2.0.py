# Author: Spencer Mae-Croft 
# Date: 08/31/2020

import sys 
import pygame

def run_game():
    # Initialize game and create a screen object. 
    pygame.init()
    window = pygame.display.set_mode((480,268))
    pygame.display.set_caption("Galaga")
    
    BGImage = pygame.image.load('BGImage.jpeg')
    

    # Start the main loop for the game
    while True:

        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        window.fill((0,0,0))
        window.blit(BGImage, (0,0))
        pygame.display.update()

        pygame.quit()
run_game()

