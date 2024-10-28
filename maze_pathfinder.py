import logging
from collections import deque
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
    logging.debug(f"rows={rows}, cols={cols}")
    destination = (rows - 1, cols - 1)
    logging.debug(f"destination={destination}")
    queue = deque()
    queue.append(starting_position)
    visited = set()
    predecessors = {starting_position: None}
    # create a graph as you explore
    while queue:
        u = queue.popleft()
        logging.debug(f"current_position={u}")

        if u == destination:
            logging.debug(f"destination reached!")
            break

        if u not in visited:
            visited.add(u)
            logging.debug(f"visiting {u}")

            for direction in directions.values():
                neighbor = move(u, direction)
                if (
                    0 <= neighbor[0] < rows
                    and 0 <= neighbor[1] < cols
                    and maze[neighbor] == 0
                    and neighbor not in visited
                ):
                    queue.append(neighbor)
                    predecessors[neighbor] = u  # Track the path
    else:
        logging.debug("terminated without reaching the destiation!")
        return []
    logging.debug(f"BFS predecessors = {predecessors}")
    # Reconstruct the path from the destination to starting_position
    logging.debug("reconstructing the path from the predecessors list")
    path = []
    while u is not None:
        path.append(u)
        u = predecessors[u]
        logging.debug(path)
    logging.debug("finished tracing the path back to the origin!")
    logging.debug("reversing the trace to find the path")
    path.reverse()
    logging.debug(f"path:\n{path}")
    return path


if __name__ == "__main__":
    m = Maze()
    test_mazes_files = [
        "test_maze",
        "test_maze2",
        "test_large_maze",
        "test_very_large_maze",
    ]
    for maze_filename in test_mazes_files:
        print(maze_filename)
        m.read_from_csv(maze_filename)
        print(m)
        p = maze_pathfinder(m)
        print(f"path: {p}")
