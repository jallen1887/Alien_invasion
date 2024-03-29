""" Class for the bullets in Alien Invasion game """

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ Bullets for Alien Invasion """

    def __init__(self, ai_settings, screen, ship):
        """ create a bullet at the ship's current position """
        super(Bullet, self).__init__()
        self.screen = screen

        # Creating a bullet rect at (0,0) and then set coreect position.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store bullet's position as decimal value
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """ move the bullet up the screen """
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """ Draw the bullet to the screen """
        pygame.draw.rect(self.screen, self.color, self.rect)
