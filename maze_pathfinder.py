import logging
from maze import Maze

# configure basic logging
logging.basicConfig(filename="debug_pathfinder.log", level=logging.DEBUG)


def move(current_position, direction):
    return (current_position[0] + direction[0], current_position[1] + direction[1])


def maze_pathfinder(maze: Maze, starting_position=(0, 0)):
    """Given a Maze object, finds a path from 0,0 to the square (n-1,m-1),
    where the maze is assumed to be of size nxm"""
    logging.debug(f"input maze:\n{maze}")
    logging.debug(f"input starting_position={starting_position}")
    directions = {"Up": (1, 0), "Down": (-1, 0), "Left": (0, -1), "Right": (0, 1)}
    rows, cols = maze.dimensions()


if __name__ == "__main__":
    m = Maze()
    m.read_from_csv("test_maze")
    maze_pathfinder(m)
