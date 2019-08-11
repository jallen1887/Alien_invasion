""" Testing the outputs of key presses in pygame """

import sys
import pygame

def run_game():
    """ main function of the game """

    pygame.init()
    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption("Test")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)

        pygame.display.flip()

run_game()
