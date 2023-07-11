from menus.menu import *


class CreditsMenu(Menu):
    """
    Represents the credits menu in the application.
    Inherits from the Menu class.
    """

    def __init__(self, app):
        Menu.__init__(self, app)

    def display_menu(self):
        """
        Displays the credits menu and handles user input.
        While the run_display flag is True, the method checks for user events.
        If the BACK_KEY or START_KEY is pressed, the current menu is changed to the main menu.
        The display is filled with a black color, and the text "Credits" and the credits information
        are drawn on the screen.
        """
        self.run_display = True

        while self.run_display:
            self.app.check_events()

            if self.app.BACK_KEY or self.app.START_KEY:
                self.app.curr_menu = self.app.main_menu
                self.run_display = False

            self.app.display.fill(settings.BLACK)
            self.app.draw_text('Credits', 30, settings.SCREEN_WIDTH / 2,
                               settings.SCREEN_HEIGHT / 2 - 20)
            self.app.draw_text('Made by Daniil Palagin', 20, settings.SCREEN_WIDTH / 2,
                               settings.SCREEN_HEIGHT / 2 + 20)
            self.blit_screen()

