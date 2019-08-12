""" Module for the button class to start the game Alien Invasion """

import pygame.font

class Button():
    """ Button class """
    def __init__(self, ai_settings, screen, msg):
        """ Initialize button attributes """
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set dimension and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Prep the button msg once
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """ Turn msg into rendered image and center text on button """
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """ Draw blank button then message """
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
