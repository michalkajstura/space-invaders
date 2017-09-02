class Settings():
    """ Settings for Alien Invasion"""
    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800

        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

        # ship's velocity
        self.velocity = 10
        # bullet setting
        self.bullet_velocity = 10
        # alien velocity
        self.alien_velocity = 0.5

        self.bullet_width = 5
        self.bullet_height = 20

        self.bullet_color = (0, 255, 0)
        self.alien_bullet_color = (255, 0, 0)

        # Maximum amount of bullets on screen
        self.max_bullets = 5

        # ship and alien size
        self.ship_size = 50
        self.alien_size = 40

        # space between two alien ships
        self.spacing_x = 2
        self.spacing_y = 0.4

        # margin
        self.margin = 6

        # how many rows of aliens
        self.number_of_rows = 4

        # how many seconds betweed shots
        self.shooting_time = 3



