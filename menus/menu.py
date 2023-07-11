import pygame

import settings


class Menu:
    """
    Represents a base menu class in the application.
    Attributes:
        app (Application): The main application object.
        mid_w (float): The x-coordinate of the middle of the screen.
        mid_h (float): The y-coordinate of the middle of the screen.
        run_display (bool): Flag indicating whether the menu is currently being displayed.
        cursor_rect (pygame.Rect): Rectangle representing the cursor position on the screen.
        offset (int): Offset value for positioning elements.

    """
    def __init__(self, app):
        self.app = app
        self.mid_w, self.mid_h = settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

    def draw_cursor(self):
        """
        Draws the cursor at its current position.
        Uses the draw_text method of the application to draw a cursor symbol at the x and y coordinates
        of the cursor_rect.
        """
        self.app.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        """
        Blits the display onto the screen and updates the display.
        Blits the display surface onto the screen surface at position (0, 0).
        Then, updates the display to reflect the changes.
        Finally, resets the internal state of the application.
        """
        self.app.screen.blit(self.app.display, (0, 0))
        pygame.display.update()
        self.app.reset()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startX, self.startY = settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT / 2 + 20
        # self.optionX, self.optionY = settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT / 2 + 50
        self.creditsX, self.creditsY = settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT / 2 + 50
        self.exitX, self.exitY = settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT / 2 + 80
        self.cursor_rect.midtop = (self.startX + self.offset, self.startY)

    def display_menu(self):
        self.run_display = True

        while self.run_display:
            self.app.check_events()
            self.check_input()
            self.app.display.blit(self.app.bg, (0, 0))
            self.app.draw_text('AI ROBO', 30, settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT / 2 - 30)
            self.app.draw_text('Start Game', 20, self.startX, self.startY)
            # self.app.draw_text('Option', 20, self.optionX, self.optionY)
            self.app.draw_text('Credits', 20, self.creditsX, self.creditsY)
            self.app.draw_text('Exit', 20, self.exitX, self.exitY)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.app.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsX + self.offset, self.creditsY)
                self.state = 'Credits'
            # elif self.state == 'Option':
            #     self.cursor_rect.midtop = (self.creditsX + self.offset, self.creditsY)
            #     self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.exitX + self.offset, self.exitY)
                self.state = 'Exit'
            elif self.state == "Exit":
                self.cursor_rect.midtop = (self.startX + self.offset, self.startY)
                self.state = 'Start'
        elif self.app.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.exitX + self.offset, self.exitY)
                self.state = 'Exit'
            # elif self.state == 'Option':
            #     self.cursor_rect.midtop = (self.startX + self.offset, self.startY)
            #     self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startX + self.offset, self.startY)
                self.state = 'Start'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.creditsX + self.offset, self.creditsY)
                self.state = 'Credits'

    def check_input(self):
        self.move_cursor()
        if self.app.START_KEY:
            if self.state == 'Start':
                self.app.curr_menu = self.app.game_menu
            # elif self.state == 'Option':
            #     self.app.curr_menu = self.app.options_menu
            elif self.state == 'Credits':
                self.app.curr_menu = self.app.credits_menu
            elif self.state == 'Exit':
                self.app.curr_menu = None
                self.app.running = False
            self.run_display = False