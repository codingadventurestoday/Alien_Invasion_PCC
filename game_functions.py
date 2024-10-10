import sys

import pygame

def check_events():
    """respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            sys.exit()

def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen"""
    screen.fill(al_settings.bg_color)
    ship.blitme()

    #make the most recently drawn screem visible
    pygame.display.flip()