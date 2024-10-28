import logging
from collections import deque
from maze import Maze
from Graph.python.adj_list_graph import AdjacencyListGraph

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
    # create a graph as you explore
    graph = AdjacencyListGraph()
    current_position = starting_position
    while queue:
        u = queue.popleft()
        logging.debug(f"current_position={u}")
        if u == destination:
            logging.debug(f"destination reached!")
            graph.add_vertex(u)
            graph.add_edge(current_position, u)
            return graph
        if (
            u not in visited
            and u[0] >= 0
            and u[1] >= 0
            and u[0] < rows
            and u[1] < cols
            and maze[u] == 0
        ):
            logging.debug(f"visiting {u}")
            queue.append(move(u, directions["Up"]))
            queue.append(move(u, directions["Down"]))
            queue.append(move(u, directions["Left"]))
            queue.append(move(u, directions["Right"]))
            graph.add_vertex(u)
            graph.add_edge(current_position, u)
        visited.add(u)
    logging.debug("terminated without reaching the destiation!")
    return graph


if __name__ == "__main__":
    m = Maze()
    m.read_from_csv("test_maze")
    maze_pathfinder(m)
