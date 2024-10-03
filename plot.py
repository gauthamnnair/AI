import random
import numpy as np
import matplotlib.pyplot as plt
from algo import dfs, bfs, a_star  # Import algorithms

def create_maze(width, height):
    maze = [['#' for _ in range(width)] for _ in range(height)]
    directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]

    def dfs_gen(x, y):
        maze[y][x] = ' '
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 < nx < width and 0 < ny < height and maze[ny][nx] == '#':
                maze[y + dy // 2][x + dx // 2] = ' '
                dfs_gen(nx, ny)

    dfs_gen(1, 1)

    # Create specific paths to ensure different algorithm behaviors
    maze[3][5] = ' '
    maze[5][5] = ' '
    maze[6][5] = ' '
    maze[6][6] = '#'
    maze[3][4] = ' '
    maze[4][4] = ' '
    maze[5][4] = ' '
    maze[1][0] = 'S'
    maze[height - 2][width - 1] = 'E'
    return maze

def generate_unique_maze(width, height):
    while True:
        maze = create_maze(width, height)
        dfs_path = dfs(maze)[0]
        bfs_path = bfs(maze)[0]
        a_star_path = a_star(maze)[0]

        if (dfs_path and bfs_path and a_star_path):
            if (dfs_path != bfs_path and
                dfs_path != a_star_path and
                bfs_path != a_star_path):
                return maze
            else:
                print("Paths are the same, trying again...")

def plot_maze(maze):
    height = len(maze)
    width = len(maze[0])
    grid = np.zeros((height, width))

    for y in range(height):
        for x in range(width):
            if maze[y][x] == '#':
                grid[y, x] = 1  # Wall

    plt.imshow(grid, cmap='binary')
    plt.xticks([])
    plt.yticks([])
    plt.savefig('maze.png', bbox_inches='tight', dpi=300)
    plt.close()

def save_maze_to_file(maze, filename='maze.txt'):
    with open(filename, 'w') as f:
        for row in maze:
            f.write(''.join(row) + '\n')

def main():
    width, height = 51, 51
    maze = generate_unique_maze(width, height)

    save_maze_to_file(maze)
    plot_maze(maze)

    for row in maze:
        print(''.join(row))

if __name__ == "__main__":
    main()
