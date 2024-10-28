"""This module provides a maze representation based on a binary matrix,
it also provides some facilities for reading/writing mazes to files"""

import csv


class Maze:
    def __init__(self, maze_grid=[]):
        self.grid = maze_grid

    def write_to_csv(self, filename):
        """Writes the maze to a csv file named filename"""
        with open(filename, "w+") as file:
            maze_writer = csv.writer(file, dialect="unix")
            maze_writer.writerows(self.grid)

    def read_from_csv(self, filename):
        """Reads a maze from a csv file named filename"""
        with open(filename, "r") as file:
            maze_reader = csv.reader(file, dialect="unix")
            self.grid = []
            for row in maze_reader:
                self.grid.append([int(e) for e in row])

    def __getitem__(self, index):
        if isinstance(index, tuple) and len(index) == 2:
            row, col = index
            return self.grid[row][col]
        else:
            raise IndexError(
                "number of indices doesn't match the dimensions of the grid"
            )

    def dimensions(self):
        """Returns the dimensions of the maze"""
        return len(self.grid), len(self.grid[0])

    def __repr__(self) -> str:
        s = "\n".join([" ".join(map(str, line)) for line in self.grid])
        return s


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
    print(m[4, 4])
    print("write it to a file!")
    m.write_to_csv("test")
    print("read it back! ")
    a = Maze()
    a.read_from_csv("test")
    print("I'm like the previous guy now, look: ")
    print(a)
    print(f"Here are my dimensions: {a.dimensions()}")
