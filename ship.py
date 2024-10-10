import pygame

class Ship():
    def __init__(self, screen):
        """Initialize the ship and set its starting positioning"""
        self.screen = screen

        #load the ship image and get its rect
        self.image = pygame.image.load("./img/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect - screen.get_rect()

        #start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen.rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)