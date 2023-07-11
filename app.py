from settings import *

from menus.options_menu import *
from menus.credits_menu import *
from menus.game_menu import *
from gamePackage.info_game import *
from menus.settings_game_menu import *
from gamePackage.coop_game import *
from gamePackage.mute_game import *


class Application:
    def __init__(self):
        """ Main Game class for initializing all demanding classes, putting
            dependencies"""
        # initialize pygame
        pygame.init()
        # initialize window
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        # fill window with black color
        self.screen.fill(settings.BLACK)
        # initialize surface
        self.display = pygame.Surface([SCREEN_WIDTH, SCREEN_HEIGHT])
        # set caption for app
        pygame.display.set_caption('AI ROBO')

        # initialize clock for FPS limit
        self.clock = pygame.time.Clock()
        # states of the app
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.LEFT_KEY, self.RIGHT_KEY = False, False
        # background image
        self.bg = pygame.image.load('images/maze_image1.jpg')

        # menu
        self.main_menu = MainMenu(self)
        self.options_menu = OptionsMenu(self)
        self.credits_menu = CreditsMenu(self)
        self.volume_menu = VolumeMenu(self)
        self.video_menu = VideoMenu(self)
        self.game_menu = GameMenu(self)
        self.game_settings_menu = SettingsGameMenu(self)
        self.curr_menu = self.main_menu

        # filename for the game
        self.filename_map = None

        # settings for the game
        self.game_amount_robots = None
        self.mode = None

    def game_loop(self):
        """Main Game Loop"""
        game = None
        score_screen = False
        steps = 0
        if self.playing:
            if self.mode == "Information":
                game = InfoGame(self.filename_map,
                                self.display)
            elif self.mode == "Cooperation":
                game = CoopGame(self.filename_map, self.display)
            elif self.mode == "Mute":
                game = MuteGame(self.filename_map, self.display)
            game.load()
        self.display.fill((0, 0, 0))
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False

            if len(game.mazes) == 0:
                self.playing = False
                score_screen = True
            if game is not None:
                game.step()
            steps += 1
            self.screen.blit(self.display, (0, 0))
            pygame.display.update()
            self.reset()
            self.clock.tick(20)
        self.display.fill((0, 0, 0))
        while score_screen:
            self.check_events()
            if self.START_KEY:
                score_screen = False
            self.draw_text(f"Score {steps} steps", 30, settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT / 2)
            self.screen.blit(self.display, (0, 0))
            pygame.display.update()
            self.reset()
            self.clock.tick(15)

    def check_events(self):
        """The check_events method is responsible for handling user input events.
         It loops over all events in the event queue obtained from pygame.event.get().
        If the event type is pygame.QUIT, it sets the running and playing variables
        to False and also updates self.main_menu.run_display to False. If the event type is
        pygame.KEYDOWN, it checks for specific key presses and sets the corresponding
        key variables (START_KEY, BACK_KEY, DOWN_KEY, UP_KEY, LEFT_KEY, RIGHT_KEY) to
        True accordingly. This method allows the game to respond to user input, such as
         quitting the game or detecting key presses for specific actions."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.main_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_LEFT:
                    self.LEFT_KEY = True
                if event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY = True

    def reset(self):
        """The reset method is used to reset the state of the key
        variables in the Application class. It sets all the key
        variables (UP_KEY, DOWN_KEY, START_KEY, BACK_KEY, LEFT_KEY,
        RIGHT_KEY) to False. This method is typically
        called after processing user input in order to reset the
        state of the keys for the next iteration or frame of
        the game loop."""
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.LEFT_KEY, self.RIGHT_KEY = False, False, False, False, False, False

    def draw_text(self, text, size, x, y):
        """
        The draw_text method is responsible for rendering and
        displaying text on the screen. It takes the parameters text
        (the content of the text), size (the font size), x (the x-coordinate),
        and y (they-coordinate). The method creates a font object using the
        specified font name and size. It renders the text onto a surface with
        the chosen font, text color (white in this case), and background color
        (transparent). A rectangle is created to represent the position and
        dimensions of the rendered text. The center of the rectangle is set
        to the specified (x, y) coordinates. Finally, the rendered text surface
        is blitted (drawn) onto the self.display surface at the specified
        rectangle's position.
        """
        font = pygame.font.Font(settings.F8_BIT_FONT_NAME, size)
        text_surface = font.render(text, True, settings.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)
