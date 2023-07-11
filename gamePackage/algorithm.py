"""
This module provides various utility functions for heap operations,
copying objects, and generating random values.
"""
import heapq
import copy
import random


# These lists represent the offsets for the four cardinal directions: up, right, down, and left.
X = [0, 1, 0, -1]
Y = [-1, 0, 1, 0]


def is_valid(pos_x, pos_y, maze):
    """The isValid function checks if a given position (x, y)
    is within the boundaries of the maze and does not
    contain an obstacle denoted by the letter 'X'.
    Returns True if the position is valid, False otherwise."""
    return 0 <= pos_y < len(maze) and 0 <= pos_x < len(maze[pos_y]) and maze[pos_y][pos_x] != 'X'


def get_neighbors(current, maze):
    """The getNeighbors function takes a current cell
    and the maze as input and returns a list of valid neighboring
    cells. It iterates over the four cardinal directions using
    the offsets from X and Y lists, calculates the coordinates of
    each neighbor, and checks their validity using the isValid function.
    The valid neighbors are stored in the neighbors list and returned."""
    neighbors = []
    for k in range(4):
        pos_dx = current[1] + X[k]
        pos_dy = current[0] + Y[k]
        if is_valid(pos_dx, pos_dy, maze):
            neighbors.append((pos_dy, pos_dx))
    return neighbors


def manhattan_distance(cell1, cell2):
    """The manhattan_distance function calculates the
    Manhattan distance between two cells given their coordinates.
    It computes the absolute difference between the x-coordinates
    and the absolute difference between the
    y-coordinates, and returns their sum."""
    return abs(cell1[0] - cell2[0]) + abs(cell1[1] - cell2[1])


def a_star(mazer, robot, maze):
    """The aStar function implements the A* search algorithm
    to find the optimal path from the robot's position to
    the mazer's position in the given maze."""
    maze = copy.deepcopy(maze)
    path_length = 0

    queue = []
    start = (robot.y, robot.x)
    goal = (mazer.y, mazer.x)
    # initialize a dictionary to keep track of the f-score of each cell
    f_scores = {start: manhattan_distance(start, goal)}

    # initialize a dictionary to keep track of the g-score of each cell
    g_scores = {start: 0}

    # initialize a dictionary to keep track of the parent cell of each cell in the optimal path
    parents = {}

    # add the start cell to the priority queue with priority equal to its f-score
    heapq.heappush(queue, (f_scores[start], start))

    while queue:
        # pop the cell with the lowest f-score from the priority queue
        _, current_cell = heapq.heappop(queue)
        if current_cell == goal:
            path = [goal]
            while path[-1] != start:
                path.append(parents[path[-1]])
                path_length += 1
            path.reverse()
            robot.path = path
            return path_length
        neighbors = get_neighbors(current_cell, maze)

        for neighbor in neighbors:
            # calculate the tentative g-score of the neighbor
            tentative_g_score = g_scores[current_cell] + 1
            # if the neighbor has not been visited yet, or the tentative g-score
            # is lower than its previous g-score:
            if neighbor not in g_scores or tentative_g_score < g_scores[neighbor]:
                # update the g-score and f-score of the neighbor
                g_scores[neighbor] = tentative_g_score
                f_scores[neighbor] = tentative_g_score + manhattan_distance(neighbor, goal)

                # set the parent of the neighbor to the current cell
                parents[neighbor] = current_cell

                # add the neighbor to the priority queue with priority equal to its f-score
                heapq.heappush(queue, (f_scores[neighbor], neighbor))
    robot.path = []
    return None


def set_diff(info, maze):
    """
    Returns a list of unvisited cells by comparing the cells in
    the maze with the visited cells in the info array.
    Args:
        info (list): A list of visited cells.
        maze (list): The maze grid.
    Returns:
        list: A list of unvisited cells.
    """
    visited = set(info)  # Convert the info array to a set for faster lookup
    unvisited = []
    # Iterate over each cell in the maze
    for pos_y, row in enumerate(maze):
        for pos_x, _ in enumerate(row):
            current_cell = (pos_y, pos_x)
            if current_cell not in visited and is_valid(pos_x, pos_y, maze):
                unvisited.append(current_cell)
    return unvisited


def find_nearest_cell(robot, unvisited):
    """
    Finds the nearest cell to the robot's current position from the list of unvisited cells.
    Args:
        robot (Robot): The robot object representing the current position and state of the robot.
        unvisited (list): A list of unvisited cells.
    Returns:
         tuple: The coordinates of the nearest cell.

        """
    min_distance = float('inf')
    nearest_cell = None
    for cell in unvisited:
        distance = manhattan_distance((robot.y, robot.x), cell)
        if distance < min_distance:
            min_distance = distance
            nearest_cell = cell
    return nearest_cell


class Cell:
    """
    Class that represents a single cell
    Usually using for a_star algorithm
    """
    def __init__(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y

    def pos(self):
        """
        :return: A tuple of x and y
        """
        return self.x, self.y

    def __str__(self):
        return f"Cell: x:{self.x}, y: {self.y}"


def prior_searching(robot, info, maze):
    """
      Performs prior searching by finding the nearest unvisited cell to the robot's current
      position, and executing the A* algorithm to navigate to that cell in the maze.
      Args:
      robot (Robot): The robot object representing the current position and state of the robot.
        info (list): A list of visited cells.
        maze (Maze): The maze object representing the layout of the maze.
      Returns:
        list: A list of unvisited cells after the prior searching operation.

      """
    unvisited = set_diff(info, maze)
    nearest_cell = find_nearest_cell(robot, unvisited)
    if nearest_cell is None:
        nearest_cell = random.choice(unvisited)
    nearest_cell_obj = Cell(nearest_cell[1], nearest_cell[0])
    a_star(nearest_cell_obj, robot, maze)
    if not robot.path:
        robot.explored_cells.append(nearest_cell)
    return unvisited
