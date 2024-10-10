import pygame

class Ship():
    def __init__(self, screen):
        """Initialize the ship and set its starting positioning"""
        self.screen = screen

        #load the ship image and get its rect
        self.image = pygame.image.load("./img/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Movement flag
        self.moving_right = False
        self.moving_left = False

        #start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def update(self):
        """Update the ship's position based on movement flag"""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)