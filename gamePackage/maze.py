"""
Imports:
- The 'floor' function from the 'math' module for rounding down decimal numbers.
- The 'pygame' module for creating games and graphics.
- The 'settings' module for accessing game settings.
"""

from math import floor
import pygame
import settings


class Maze:
    """Class Maze is for creating maze using txt file as an input. Provides different methods"""

    def __init__(self, display):
        self.display = display
        self.maze_map = []
        settings.CELL_WIDTH = floor(settings.SCREEN_WIDTH / settings.MAZE_WIDTH)
        settings.CELL_HEIGHT = floor(settings.SCREEN_HEIGHT / settings.MAZE_HEIGHT)
        self.texture_wall = None
        self.texture_robot = None
        self.texture_house = None
        self.texture_mazer = None
        self.textures_load()

    def draw(self):
        """
           Draws the maze based on the values in the maze_map attribute.

           The maze is drawn by iterating over each row and column of the maze_map.
           - If a cell contains 'X', a Cell object with a black color is created and drawn.
           - If a cell contains 'R', the texture_robot image is blitted at the corresponding
             position.
           - If a cell contains 'M', the texture_mazer image is blitted at the corresponding
             position.
           - If a cell contains '0', a Cell object with a blue color is created and drawn.
           - For any other value, a Cell object with a white color is created and drawn.
           """
        for pos_y, row in enumerate(self.maze_map):
            for pos_x, _ in enumerate(row):
                if self.maze_map[pos_y][pos_x] == 'X':
                    pygame.draw.rect(self.display, settings.BLACK,
                                     [pos_x * settings.CELL_WIDTH,
                                      pos_y * settings.CELL_HEIGHT, settings.CELL_WIDTH,
                                      settings.CELL_HEIGHT])
                elif self.maze_map[pos_y][pos_x] == 'R':
                    self.display.blit(self.texture_robot,
                                      [pos_x * settings.CELL_WIDTH, pos_y * settings.CELL_HEIGHT])
                elif self.maze_map[pos_y][pos_x] == 'M':
                    self.display.blit(self.texture_mazer,
                                      [pos_x * settings.CELL_WIDTH, pos_y * settings.CELL_HEIGHT])
                elif self.maze_map[pos_y][pos_x] == '0':
                    pygame.draw.rect(self.display, settings.BLUE,
                                     [pos_x * settings.CELL_WIDTH,
                                      pos_y * settings.CELL_HEIGHT, settings.CELL_WIDTH,
                                      settings.CELL_HEIGHT])
                else:
                    pygame.draw.rect(self.display, settings.WHITE,
                                     [pos_x * settings.CELL_WIDTH,
                                      pos_y * settings.CELL_HEIGHT, settings.CELL_WIDTH,
                                      settings.CELL_HEIGHT])

    def textures_load(self):
        """Loads and scales the textures for walls, robot, house, and mazer in the maze."""
        self.texture_wall = pygame.image.load("./images/wall.jpg")
        self.texture_wall = pygame.transform.scale(self.texture_wall,
                                                   (settings.CELL_WIDTH, settings.CELL_HEIGHT))
        self.texture_robot = pygame.image.load("./images/robot1.jpg")
        self.texture_robot = pygame.transform.scale(self.texture_robot,
                                                    (settings.CELL_WIDTH, settings.CELL_HEIGHT))
        self.texture_house = pygame.image.load("./images/house.png")
        self.texture_house = pygame.transform.scale(self.texture_house,
                                                    (settings.CELL_WIDTH, settings.CELL_HEIGHT))
        self.texture_mazer = pygame.image.load("./images/box.png")
        self.texture_mazer = pygame.transform.scale(self.texture_mazer,
                                                    (settings.CELL_WIDTH, settings.CELL_HEIGHT))
