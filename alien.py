""" Alien class for the Alien Invasion game """

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ A class to represent Aliens in Alien invasion """

    def __init__(self, ai_settings, screen):
        """ initialize alien and set its starting position """
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load image of the alien
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # start each alien at the top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the alien's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """ draw the alien at its current loaction """
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """ Return True if alien is at the edge of screen """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        if self.rect.left <= 0:
            return True

        return False

    def update(self):
        """ Move the alien right or left"""
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x
