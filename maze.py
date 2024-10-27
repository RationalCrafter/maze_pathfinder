"""This module provides a maze representation based on a binary matrix,
it also provides some facilities for reading/writing mazes to files"""

import csv


class Maze:
    def __init__(self, maze_grid=[]):
        self.grid = maze_grid

    def write_to_csv(self, filename):
        """Writes the maze to a csv file named filename"""
        with open(filename, "w+") as file:
            maze_writer = csv.writer(file)
            maze_writer.writerows(self.grid)

    def read_from_csv(self, filename):
        """Reads a maze from a csv file named filename"""
        with open(filename, "r") as file:
            maze_reader = csv.reader(file)
            self.grid = []
            for row in maze_reader:
                self.grid.append([int(e) for e in row])

    def __getitem__(self, index):
        if isinstance(index, tuple) and len(index) == 2:
            row, col = index
            return self.grid[row][col]

    def __repr__(self) -> str:
        return self.grid.__repr__()


if __name__ == "__main__":
    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [1, 1, 1, 1, 0],
    ]
    m = Maze(maze_grid=maze)
    print(m)
    print(m[1, 2])
    print("write it to a file!")
    m.write_to_csv("test")
    print("read it back! ")
    a = Maze()
    a.read_from_csv("test")
    print("I'm like the previous guy now, look: ")
    print(a)
