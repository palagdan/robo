from gamePackage.game import *
from gamePackage.algorithm import a_star, prior_searching


class MuteGame(Game):
    """
    Subclass of Game that represents the mute mode.
    This class extends the Game class and implements additional
    functionality specific to the mute mode of the game.
    """

    def __init__(self, filename, display):
        super().__init__(filename, display)

    def step(self):
        """
        Perform a step in the mute mode game.
        Updates the game state by checking and updating the state of the
        robots, moving the robots, controlling mazes,
        updating the map, and drawing the maze.

        This method also checks if all mazes have been delivered and sets the
        is_running flag accordingly.
        """
        if len(self.mazes) == 0:
            self.is_running = False
        self.steps += 1

        # assign next cell for exploring and adding information
        self.check_state()
        # move robots
        self.move_robots()

        # control mazes
        self.control_mazes()

        # update map
        self.update()

        self.maze_class.draw()

    def check_state(self):
        """
        Check and update the state of the robots in the mute mode.

        Performs state checks for each robot and updates their attributes and
        states based on the current game state and robot positions.

        Robots in the EXPLORING state will transition to the WAITING state if
        their path is empty.
        Robots in the WAITING state will perform a prior searching algorithm to
        explore new cells.
        Robots in the DELIVERING state will update their target maze as delivered and
        collect any new mazes found.
        """

        for robot in self.robots:
            x, y = robot.pos()
            if self.maze_class.maze_map[y][x] == 'M' and robot.state != RobotState.DELIVERING:
                robot.target = self.get_mazes_by_pos((y, x))
                robot.target.collected = True
                robot.state = RobotState.DELIVERING
                robot.path.clear()
            elif robot.state == RobotState.DELIVERING:
                if self.maze_class.maze_map[y][x] == 'M':
                    robot.mazes_found.append(self.get_mazes_by_pos((y, x)))
                    print(self.get_mazes_by_pos((y, x)))
            elif robot.state == RobotState.EXPLORING and len(robot.path) == 0:
                robot.state = RobotState.WAITING
            elif robot.state == RobotState.WAITING:
                prior_searching(robot, robot.explored_cells, self.maze_class.maze_map)
                robot.state = RobotState.EXPLORING

    def move_robots(self):
        """
        Move the robots in the mute mode.
        Moves the robots based on their current state and path in the mute mode.
        If a robot is in the DELIVERING state and has an empty path, a new path
        is calculated from the collecting point to the robot's current position.
        If a robot is in the COLLECTING state and has an empty path but has found new mazes,
        the robot will select the maze with the shortest path and move towards it.
        Robots in the EXPLORING or WAITING state will move without a target.
        The move_mute() method is called on each robot to update its internal state.
        """
        for robot in self.robots:
            if robot.state == RobotState.DELIVERING and robot.path == []:
                a_star(self.collecting_point, robot, self.maze_class.maze_map)
                robot.move_mute()
            elif robot.state == RobotState.COLLECTING and robot.path == [] and robot.mazes_found:
                min_mazes = None
                min_counter = 10000000
                for mazes in robot.mazes_found:
                    tmp = a_star(mazes, robot, self.maze_class.maze_map)
                    if tmp < min_counter:
                        min_counter = tmp
                        min_mazes = mazes
                robot.mazes_found.remove(min_mazes)
                robot.move_mute()
            else:
                robot.move_mute()
