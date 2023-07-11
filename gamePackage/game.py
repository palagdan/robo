from gamePackage.maze import *
from gamePackage.collecting_point import *
from gamePackage.mazes import *
from gamePackage.robot import *


class Game:
    """Base class for different types of games."""

    def __init__(self, filename, display):
        self.filename = filename
        self.robots = []  # List to store robot objects
        self.mazes = []  # List to store maze objects
        self.mazes_uncollected = []  # List to store mazes that have not been collected yet
        self.collecting_point = None  # Object representing the collecting point
        self.is_running = True  # Flag indicating if the game is running
        self.maze_class = Maze(display)  # Instance of the Maze class for handling maze-related operations
        self.steps = 0  # Counter to keep track of the number of steps taken in the game
        self.display = display  # The display surface for rendering the game
        self.mazes_pos_db = {}

    def load(self):
        """
        Load the game data from the specified file.
        Reads the file line by line and creates robot, maze, and collecting
        point objects.
        Updates the maze map and related properties.
        """
        # Load the game data from the specified file
        with open(self.filename, 'r') as file:
            for y, line in enumerate(file):
                maze_line = []
                for x, char in enumerate(line.strip()):
                    maze_line.append(char)
                    if char == "R":
                        # Create a robot object and add it to the list of robots
                        self.robots.append(Robot(x, y))
                    if char == "M":
                        # Create a maze object and add it to the list of mazes and mazes_uncollected
                        mazer = Mazes(x, y)
                        self.mazes.append(mazer)
                        self.mazes_uncollected.append(mazer)
                        self.mazes_pos_db[(y, x)] = mazer
                    if char == "0":
                        # Create a collecting point object
                        self.collecting_point = CollectingPoint(x, y)
                self.maze_class.maze_map.append(maze_line)

        # Update the rowLength properties of the maze_class
        self.maze_class.rowLength = len(self.maze_class.maze_map)
        self.maze_class.rowLength = len(self.maze_class.maze_map[0])

    def update(self):
        """
         Update the game state and map.
         Clears the maze map and updates it with the current positions
         of robots, mazes, and the collecting point.
        """
        # Clear the maze map
        for row in self.maze_class.maze_map:
            for i in range(len(row)):
                if row[i] == 'R':
                    row[i] = ' '  # Remove the previous robot symbol 'R'
        # Update the maze map with robot positions
        for robot in self.robots:
            x, y = robot.pos()
            self.maze_class.maze_map[y][x] = 'R'
        for maze in self.mazes:
            x, y = maze.pos()
            if maze.collected:
                self.maze_class.maze_map[y][x] = ' '
            else:
                self.maze_class.maze_map[y][x] = 'M'
        x, y = self.collecting_point.pos()
        self.maze_class.maze_map[y][x] = '0'

    def control_mazes(self):
        """
        Control the state of the mazes.
        Removes delivered mazes from the list of mazes.
        """
        for maze in self.mazes:
            if maze.delivered:
                self.mazes.remove(maze)

    def get_mazes_by_pos(self, pos):
        """Get maze objects based on their positions."""
        return self.mazes_pos_db[(pos[0], pos[1])]
