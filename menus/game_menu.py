from menus.menu import *
from os import listdir
from os.path import isfile, join
import settings


class GameMenu(Menu):

    def __init__(self, app):
        Menu.__init__(self, app)
        self.maps = [f for f in listdir(settings.MAPS_PATH) if isfile(join(settings.MAPS_PATH, f))]
        self.state = self.maps[0]
        self.length_maps = len(self.maps)
        self.curr_index = 0
        self.curr_height = settings.SCREEN_HEIGHT / 2 + 20
        self.cursor_rect.midtop = (settings.SCREEN_WIDTH / 2 + self.offset, settings.SCREEN_HEIGHT / 2 + 20)

    def display_menu(self):
        self.run_display = True

        while self.run_display:
            self.app.check_events()
            self.check_input()
            self.app.display.fill(settings.BLACK)
            self.app.draw_text('Choose the map', 30, settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT / 2 - 30)
            height = settings.SCREEN_HEIGHT / 2 + 20
            for map in self.maps:
                map_without_txt, _ = map.split('.')
                self.app.draw_text(map_without_txt, 15, settings.SCREEN_WIDTH / 2, height)
                height += 30
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.app.DOWN_KEY and self.curr_index != self.length_maps - 1:
            self.curr_height += 30
            self.curr_index += 1
            self.cursor_rect.midtop = (settings.SCREEN_WIDTH / 2 + self.offset, self.curr_height)
            self.state = self.maps[self.curr_index % self.length_maps]
        elif self.app.UP_KEY and self.curr_index != 0:
            self.curr_height -= 30
            self.curr_index -= 1
            self.cursor_rect.midtop = (settings.SCREEN_WIDTH / 2 + self.offset, self.curr_height)
            self.state = self.maps[self.curr_index % self.length_maps]

    def check_input(self):
        self.move_cursor()
        if self.app.BACK_KEY:
            self.app.curr_menu = self.app.main_menu
            self.run_display = False
        elif self.app.START_KEY:
            self.app.filename_map = f'maps/{self.state}'
            self.app.curr_menu = self.app.game_settings_menu
            self.run_display = False
