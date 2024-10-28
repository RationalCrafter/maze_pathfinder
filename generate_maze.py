import random


def generate_large_maze(n, m):
    # Step 1: Create a grid of walls (1s)
    maze_grid = [[1] * m for _ in range(n)]

    # Directions for moving (down, up, right, left)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def carve_path(x, y):
        maze_grid[x][y] = 0  # Mark the current cell as part of the maze
        random_directions = directions[:]
        random.shuffle(random_directions)

        for dx, dy in random_directions:
            nx, ny = x + dx * 2, y + dy * 2  # Move two cells away
            if 0 <= nx < n and 0 <= ny < m and maze_grid[nx][ny] == 1:
                maze_grid[x + dx][y + dy] = 0  # Remove the wall between
                carve_path(nx, ny)  # Recur for the next cell

    # Start carving from (0, 0)
    carve_path(0, 0)

    # Ensure there's a clear path to the exit at the bottom-right corner
    maze_grid[n - 1][m - 1] = 0  # Open the exit
    # Connect the last cell to the maze if needed
    if maze_grid[n - 2][m - 1] == 1:  # If the cell above is a wall, carve through it
        maze_grid[n - 2][m - 1] = 0
    if (
        maze_grid[n - 1][m - 2] == 1
    ):  # If the cell to the left is a wall, carve through it
        maze_grid[n - 1][m - 2] = 0

    return maze_grid


# Example usage
n, m = 25, 25  # Size of the maze
maze = generate_large_maze(n, m)

for row in maze:
    print(row)
