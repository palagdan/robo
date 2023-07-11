from gamePackage.game import *
from gamePackage.algorithm import a_star, prior_searching


class InfoGame(Game):
    """
    Subclass of Game that represents an informational game.
    This class extends the Game class and adds additional functionality
    for managing robot movement, maze assignments,
    and game steps.
    """
    def __init__(self, filename, display):
        super().__init__(filename, display)

    def step(self):
        """
        Perform a step in the game.
        Updates the game state by assigning mazes to free robots,
        moving robots, controlling mazes, updating the map,
        and drawing the maze.
        This method also checks if all mazes have been delivered and sets
        the is_running flag accordingly.
        """
        if len(self.mazes) == 0:
            self.is_running = False
        self.steps += 1
        free_robots = []
        # looking for free robots
        for robot in self.robots:
            if robot.target is None:
                free_robots.append(robot)
        # assign new mazes to free robots
        self.target_assign(free_robots)
        # move robots
        self.move_robots()

        # control mazes
        self.control_mazes()

        # update map
        self.update()

        self.maze_class.draw()

    def move_robots(self):
        """
        Move the robots based on their current state and path.
        Moves the robots to their target positions by utilizing the
        A* pathfinding algorithm.
        If a robot is in the DELIVERING state and has an empty path, a new path is
        calculated from the collecting point to the robot's current position.
        If a robot is not in the DELIVERING state or has a non-empty path,
        the robot is moved to the next position in its path.
        The move_info() method is called on each robot to update its internal state.
        """
        for robot in self.robots:
            if robot.state == RobotState.DELIVERING and robot.path == []:
                a_star(self.collecting_point, robot, self.maze_class.maze_map)
                robot.move_info()
            else:
                robot.move_info()

    def target_assign(self, robots):
        """Assign mazes to free robots.
        Assigns mazes from the list of uncollected mazes to the available
        free robots.
        The assignment is based on the result of the A* pathfinding algorithm,
        which calculates the shortest path from each free robot to each uncollected maze."""
        if len(robots) == 0:
            return
        if len(self.mazes) == 0:
            return
        for mazer in self.mazes_uncollected:
            min_robot = None
            min_counter = 10000000
            if len(robots) == 0:
                return
            for robot in robots:
                result = a_star(mazer, robot, self.maze_class.maze_map)
                if result is None:
                    continue
                if result < min_counter:
                    min_counter = result
                    min_robot = robot
                    min_robot.target = mazer
            if min_robot is not None:
                robots.remove(min_robot)
                min_robot.state = RobotState.COLLECTING
                self.mazes_uncollected.remove(min_robot.target)
