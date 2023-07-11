from menus.menu import *


class OptionsMenu(Menu):
    """
    Represents the options menu in the application.
    Inherits from the Menu class.
    """
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volX, self.volY = self.mid_w, self.mid_h + 20
        self.videoX, self.videoY = self.mid_w, self.mid_h + 50

    def display_menu(self):
        """
        Displays the options menu and handles user input.
        While the run_display flag is True, the method checks for user events and input.
        The display is filled with a black color, and the text "Options", "Volume", and "Video"
        are drawn on the screen. The cursor is drawn at the current state position.
        """
        self.run_display = True
        while self.run_display:
            self.app.check_events()
            self.check_input()
            self.app.display.fill(settings.BLACK)
            self.app.draw_text('Options', 30, settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT / 2 - 20)
            self.app.draw_text('Volume', 20, self.volX, self.volY)
            self.app.draw_text('Video', 20, self.videoX, self.videoY)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        """
        Checks the user input and performs corresponding actions.
        """
        if self.app.BACK_KEY:
            self.app.curr_menu = self.app.main_menu
            self.run_display = False
        elif self.app.UP_KEY or self.app.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Video'
                self.cursor_rect.midtop = (self.videoX + self.offset, self.videoY)
            elif self.state == 'Video':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volX + self.offset, self.volY)
        elif self.app.START_KEY:
            if self.state == 'Volume':
                self.app.curr_menu = self.app.volume_menu
            elif self.state == 'Video':
                self.app.curr_menu = self.app.video_menu
            self.run_display = False


class VolumeMenu(Menu):
    """
     Represents the volume menu in the application.
     Inherits from the Menu class.
    """
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        """Displays the volume menu and handles user input."""
        self.run_display = True
        while self.run_display:
            self.app.check_events()
            self.check_input()
            self.app.display.fill(settings.BLACK)
            self.app.draw_text('Volume', 30, settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT / 2 - 20)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        """"""
        if self.app.BACK_KEY:
            self.app.curr_menu = self.app.options_menu
            self.run_display = False


class VideoMenu(Menu):

    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):

        self.run_display = True
        while self.run_display:
            self.app.check_events()
            self.check_input()
            self.app.display.fill(settings.BLACK)
            self.app.draw_text('Video', 30, settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT / 2 - 20)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.app.BACK_KEY:
            self.app.curr_menu = self.app.options_menu
            self.run_display = False
