
class RobotState:
    """This class defines different states that a
    robot can be in: COLLECTING, DELIVERING, and WAITING."""
    COLLECTING = "COLLECTING"
    DELIVERING = "DELIVERING"
    WAITING = "WAITING"
    EXPLORING = "EXPLORING"


class Robot:
    """This class represents a robot and its current state."""

    def __init__(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y
        self.path = []
        self.target = None
        self.state = RobotState.WAITING
        self.explored_cells = []
        self.mazes_found = []

    def move_info(self):
        """The Info move method is responsible for updating the robot's
         position based on its current state. If the robot is in the DELIVERING
         state, it moves to the next position in its path and updates its x and y coordinates.
         If the path is empty, it marks the target as delivered, sets the state to WAITING,
         and clears the target object. If the robot is in the COLLECTING state, it moves to
         the next position in its path and updates its x and y coordinates. If the path is
         empty, it marks the target as collected and changes the state to DELIVERING. If
        the robot is in any other state, it does nothing."""
        if self.state == RobotState.DELIVERING:
            if self.target is None:
                return
            self.x = self.path[0][1]
            self.y = self.path[0][0]
            del self.path[0]
            if len(self.path) == 0:
                self.target.delivered = True
                self.state = RobotState.WAITING
                self.target = None
        elif self.state == RobotState.COLLECTING:
            if self.target is None:
                return
            self.x = self.path[0][1]
            self.y = self.path[0][0]
            del self.path[0]
            if len(self.path) == 0:
                self.target.collected = True
                self.state = RobotState.DELIVERING
        else:
            return

    def add_cell(self, info):
        """
         Adds the first cell of the path to the given list 'info'.
         Parameters:
            - info: The list to which the first cell of the path will be added.
         Note:
            The 'path' attribute is assumed to be a list containing cells
            representing a path in the maze.
            """
        if not self.path:
            return
        if self.path[0] not in info:
            info.append(self.path[0])

    def move_mute(self):
        """
        Moves the robot to the next position based on its current state.
        - If the robot's state is DELIVERING:
            - The first cell of the path is assigned to the robot's current position (m_x, m_y).
            - The first cell is removed from the path.
            - If the path is empty after removing the first cell:
                - The target's 'delivered' attribute is set to True.
                - If mazes have been found (mazes_found is True):
                    - The robot's state is set to COLLECTING.
                    - The target is set to None.
                - Otherwise:
                    - The robot's state is set to WAITING.
                    - The target is set to None.
        - If the robot's state is COLLECTING:
            - If the path is empty, the robot's state is set to WAITING, the path
             is cleared, and the function returns.
            - The first cell of the path is assigned to the robot's current position (m_x, m_y).
            - The first cell is removed from the path.
        - If the robot's state is EXPLORING:
            - If the path is empty, the function returns.
            - The first cell of the path is assigned to the robot's current position (m_x, m_y).
            - The first cell is removed from the path.
        """
        self.add_cell(self.explored_cells)
        if self.state == RobotState.DELIVERING:
            self.x = self.path[0][1]
            self.y = self.path[0][0]
            del self.path[0]
            if len(self.path) == 0:
                self.target.delivered = True
                if self.mazes_found:
                    self.state = RobotState.COLLECTING
                    self.target = None
                else:
                    self.state = RobotState.WAITING
                    self.target = None
        elif self.state == RobotState.COLLECTING:
            if not self.path:
                self.state = RobotState.WAITING
                self.path.clear()
                return
            self.x = self.path[0][1]
            self.y = self.path[0][0]
            del self.path[0]
        elif self.state == RobotState.EXPLORING:
            if not self.path:
                return
            self.x = self.path[0][1]
            self.y = self.path[0][0]
            del self.path[0]

    def move_coop(self, info):
        """
           Moves the robot to the next position in cooperative mode.
           - The first cell of the path is added to the 'info' list by calling
             the 'add_cell' method.
           - If the path is empty, the function returns immediately.
           - The first cell of the path is assigned to the robot's current position (m_x, m_y).
           - The first cell is removed from the path.
           Parameters:
           - info: The list to which the first cell of the path will be added by
            calling the 'add_cell' method.
           """
        self.add_cell(info)
        if not self.path:
            return
        self.x = self.path[0][1]
        self.y = self.path[0][0]
        del self.path[0]

    def pos(self):
        """The pos method returns the current position of
        the robot as a tuple of x and y coordinates."""
        return self.x, self.y

    def __str__(self):
        return f"Robot x: {self.x} y: {self.y}"
