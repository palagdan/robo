class Mazes:
    """This class represents a maze object."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.collected = False
        self.delivered = False

    def pos(self):
        """The pos method returns the current position of the maze as a tuple of x and y coordinates."""
        return self.x, self.y

    def __str__(self):
        return f"Maze x: {self.x} y: {self.y}"
