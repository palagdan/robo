from menus.menu import *


class SettingsGameMenu(Menu):
    """ Represents the settings game menu in the application.
        Inherits from the Menu class."""
    def __init__(self, game):
        Menu.__init__(self, game)
        self.offset = self.offset - 100
        self.state = 'Amount of robots'
        self.modeX, self.modeY = self.mid_w, self.mid_h + 30

        self.cursor_rect.midtop = (self.modeX + self.offset, self.modeY)

        # state for cooperation of agents
        self.mode = ['Cooperation', 'Information', 'Mute']
        self.index_mode = 0

    def display_menu(self):
        """
        Displays the settings game menu and handles user input.
        While the run_display flag is True, the method checks for user events and input.
        The display is filled with a black color, and the text "Set the game" and the current
        mode are drawn on the screen. The cursor is drawn at the current mode position.
         """
        self.run_display = True

        while self.run_display:
            self.app.check_events()
            self.check_input()
            self.app.display.fill(settings.BLACK)
            self.app.draw_text('Set the game', 30, settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT / 2 - 20)
            self.app.draw_text(f'Mode {self.mode[self.index_mode]}',
                               15, self.modeX, self.modeY)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        """
        Checks the user input and performs corresponding actions.
        """
        if self.app.BACK_KEY:
            self.app.curr_menu = self.app.game_menu
            self.run_display = False
        elif self.app.START_KEY:
            if self.mode[self.index_mode] == 'Cooperation':
                self.app.mode = 'Cooperation'
            elif self.mode[self.index_mode] == 'Information':
                self.app.mode = 'Information'
            else:
                self.app.mode = 'Mute'
            self.app.playing = True
            self.run_display = False
        elif self.app.START_KEY:
            pass
        elif self.app.LEFT_KEY:
            self.index_mode = (self.index_mode - 1) % len(
                self.mode)
        elif self.app.RIGHT_KEY:
            self.index_mode = (self.index_mode + 1) % len(
                self.mode)
