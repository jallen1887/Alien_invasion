""" Game for shooting aliens """

import pygame

from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf

def run_game():
    """ Initialize game and create a screen object """

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    play_button = Button(ai_settings, screen, "Play")

    # Make a ship, a group of bullets and a group of aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Create an instance to store the game statistics
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Start main loop of game #
    while True:

        # Watch for mouse and keyboard events #
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_bullets(ai_settings, screen, stats, sb, ship, bullets, aliens)
        # Redraw screen through each loop #
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()
