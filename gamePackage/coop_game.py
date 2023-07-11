from gamePackage.game import *
from gamePackage.algorithm import a_star, prior_searching


class CoopGame(Game):
    """CoopGame represents the cooperative mode"""
    def __init__(self, filename, display):
        super().__init__(filename, display)
        self.path_info = []
        self.found_mazes = []

    def step(self):
        """
          Executes a single step of the simulation.
          - If there are no more mazes to explore, the simulation
            is stopped by setting 'is_running' to False.
          - The 'steps' counter is incremented by 1.
          - The state of the robots is checked and updated by calling the 'check_state' method.
          - The robots are moved to their next positions by calling the 'move_robots' method.
          - The mazes are controlled by calling the 'control_mazes' method.
          - The map is updated by calling the 'update' method.
          - The maze is drawn on the display by calling the 'draw' method
            of the 'maze_class' object.
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
           Checks and updates the state of each robot based on its current
            position and the maze conditions.
           - For each robot in the simulation, the following checks are performed:
               - If the robot is at a maze position ('M') and not already
                 in the DELIVERING state, the robot's target maze is assigned,
                  marked as collected, and the robot's state is changed to DELIVERING.
               - If the robot is in the DELIVERING state and still has a path to follow:
                   - If the robot's current position is a maze position ('M'), the maze is
                     added to the found_mazes list.
               - If the robot is in the DELIVERING state and has no more path to follow:
                   - The target maze is marked as delivered, the target is set to None,
                     and the robot's state is changed to WAITING.
               - If the robot is in the EXPLORING state and has no more path to follow:
                   - The robot's state is changed to WAITING.
               - If the robot is in the COLLECTING state and has no more path to follow:
                   - The robot's state is changed to WAITING.
               - If the robot is in the WAITING state:
                   - If there are found mazes in the simulation, the robot selects the
                     maze with the minimum path cost using the A* algorithm.
                     The robot's state is changed to COLLECTING, and the target is
                     assigned to the selected maze.
                   - If there are no found mazes, the robot performs a prior searching using the
                   'prior_searching' function and the path_info dictionary. The robot's state is
                    changed to EXPLORING.
           """
        for robot in self.robots:
            x, y = robot.pos()
            if self.maze_class.maze_map[y][x] == 'M' and robot.state != RobotState.DELIVERING:
                robot.target = self.get_mazes_by_pos((y, x))
                robot.target.collected = True
                robot.state = RobotState.DELIVERING
                robot.path.clear()
            elif robot.state == RobotState.DELIVERING and robot.path:
                if self.maze_class.maze_map[y][x] == 'M':
                    self.found_mazes.append(self.get_mazes_by_pos((y, x)))
            elif robot.state == RobotState.DELIVERING and not robot.path:
                robot.target.delivered = True
                robot.target = None
                robot.state = RobotState.WAITING
            elif robot.state == RobotState.EXPLORING and len(robot.path) == 0:
                robot.state = RobotState.WAITING
            elif robot.state == RobotState.COLLECTING and not robot.path:
                robot.state = RobotState.WAITING
            elif robot.state == RobotState.WAITING:
                if self.found_mazes:
                    min_mazes = None
                    min_counter = 10000000
                    for mazes in self.found_mazes:
                        tmp = a_star(mazes, robot, self.maze_class.maze_map)
                        if tmp < min_counter:
                            min_counter = tmp
                            min_mazes = mazes
                    self.found_mazes.remove(min_mazes)
                    robot.state = RobotState.COLLECTING
                    robot.target = min_mazes
                else:
                    prior_searching(robot, self.path_info, self.maze_class.maze_map)
                    robot.state = RobotState.EXPLORING

    def move_robots(self):
        """
            Moves the robots according to their current state and path.

            - For each robot in the simulation, the following actions are performed:
                - If the robot is in the DELIVERING state and has no more path to follow,
                  the A* algorithm is used to find a path from the robot's current
                  position to the collecting point.The robot then moves cooperatively
                  using the 'moveCoop' method with the path information.
                - For any other state, the robot moves cooperatively using the 'moveCoop'
                  method with the path information.
            """
        for robot in self.robots:
            if robot.state == RobotState.DELIVERING and robot.path == []:
                a_star(self.collecting_point, robot, self.maze_class.maze_map)
                robot.move_coop(self.path_info)
            else:
                robot.move_coop(self.path_info)
