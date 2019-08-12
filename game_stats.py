""" Module for the class to track the game stats of Alien Invasion """

class GameStats():
    """ Track statistics """

    def __init__(self, ai_settings):
        """ initialize statisitics """
        self.ai_settings = ai_settings
        self.reset_stats()

        #start Alien Invasion in an active state
        self.game_active = False

    def reset_stats(self):
        """ Reset the stats """
        self.ships_left = self.ai_settings.ship_limit
