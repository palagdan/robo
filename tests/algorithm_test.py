import pytest

from gamePackage.algorithm import *
from gamePackage.robot import *
from gamePackage.mazes import *


def test_manhattan_distance():
    # Test case 1: Cells are at the same coordinates
    assert manhattan_distance((0, 0), (0, 0)) == 0

    # Test case 2: Cells are in the same row
    assert manhattan_distance((0, 0), (0, 3)) == 3
    assert manhattan_distance((2, 5), (2, 9)) == 4

    # Test case 3: Cells are in the same column
    assert manhattan_distance((0, 0), (5, 0)) == 5
    assert manhattan_distance((7, 2), (10, 2)) == 3

    # Test case 4: Cells are in different rows and columns
    assert manhattan_distance((0, 0), (3, 4)) == 7
    assert manhattan_distance((2, 5), (7, 1)) == 9

    # Test case 5: Cells are in negative coordinates
    assert manhattan_distance((-3, -2), (1, 5)) == 11
    assert manhattan_distance((-5, 0), (0, -8)) == 13


def test_is_valid():
    maze = [
        [' ', ' ', ' ', ' '],
        [' ', 'X', ' ', ' '],
        [' ', ' ', ' ', 'X'],
        [' ', ' ', ' ', ' ']
    ]

    # Test case 1: Valid position
    assert is_valid(0, 0, maze) is True

    # Test case 2: Position out of bounds
    assert is_valid(-1, 2, maze) is False
    assert is_valid(4, 1, maze) is False

    # Test case 3: Position contains an obstacle
    assert is_valid(1, 1, maze) is False
    assert is_valid(3, 2, maze) is False

    # Test case 4: Position at the edge of the maze
    assert is_valid(0, 3, maze) is True
    assert is_valid(3, 0, maze) is True


def test_getNeighbors():
    maze = [
        [' ', ' ', ' ', ' '],
        [' ', 'X', ' ', ' '],
        [' ', ' ', ' ', 'X'],
        [' ', ' ', ' ', ' ']
    ]

    # Test case 1: Current cell is at the top-left corner of the maze
    current = (0, 0)
    expected_neighbors = [(0, 1), (1, 0)]
    assert get_neighbors(current, maze) == expected_neighbors

    # Test case 2
    current = (2, 0)
    expected_neighbors = [(1, 0), (2, 1), (3, 0)]
    assert get_neighbors(current, maze) == expected_neighbors


def test_aStar():
    maze = [
        [' ', ' ', ' ', ' '],
        [' ', 'X', ' ', ' '],
        [' ', ' ', ' ', 'X'],
        [' ', ' ', ' ', ' ']
    ]

    # Test case 1: Optimal path exists
    robot = Robot(0, 0)
    mazer = Mazes(3, 3)
    expected_path_length = 6
    assert a_star(mazer, robot, copy.deepcopy(maze)) == expected_path_length
    assert len(robot.path) == expected_path_length + 1  # Include the start cell in the path


test_is_valid()
test_manhattan_distance()
test_getNeighbors()
test_aStar()
