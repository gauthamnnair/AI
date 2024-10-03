import numpy as np
import matplotlib.pyplot as plt
from algo import dfs, bfs, a_star

def read_maze(filename):
    with open(filename, 'r') as f:
        maze = [list(line.strip()) for line in f.readlines()]
    return maze

def print_maze(maze):
    for row in maze:
        print(''.join(row))

def plot_maze_with_path(maze, final_path, backtracked_path, algo_name):
    height = len(maze)
    width = len(maze[0])
    grid = np.zeros((height, width))

    for y in range(height):
        for x in range(width):
            if maze[y][x] == '#':
                grid[y, x] = 1

    plt.imshow(grid, cmap='binary')

    if backtracked_path:
        backtracked_x, backtracked_y = zip(*backtracked_path)
        plt.scatter(backtracked_x, backtracked_y, color='red', marker='.', s=40, label='Backtracked Path')

    if final_path:
        final_x, final_y = zip(*final_path)
        plt.scatter(final_x, final_y, color='green', marker='.', s=40, label='Final Path')

    plt.xticks([])
    plt.yticks([])
    plt.title(f'Solved Maze - {algo_name}')
    plt.legend()
    plt.savefig(f'solved_maze_{algo_name}.png', bbox_inches='tight', dpi=300)
    plt.close()

def write_paths_to_file(dfs_path, bfs_path, a_star_path):
    with open('paths.txt', 'w') as f:
        f.write("DFS Path Coordinates:\n")
        f.write(', '.join(f"({x}, {y})" for x, y in dfs_path) + '\n')
        f.write("BFS Path Coordinates:\n")
        f.write(', '.join(f"({x}, {y})" for x, y in bfs_path) + '\n')
        f.write("A* Path Coordinates:\n")
        f.write(', '.join(f"({x}, {y})" for x, y in a_star_path) + '\n')

def main():
    maze = read_maze('maze.txt')
    print("Maze:")
    print_maze(maze)

    dfs_path, dfs_backtrack = dfs(maze)
    plot_maze_with_path(maze, dfs_path, dfs_backtrack, "DFS")

    maze = read_maze('maze.txt')
    bfs_path, bfs_backtrack = bfs(maze)
    plot_maze_with_path(maze, bfs_path, bfs_backtrack, "BFS")

    maze = read_maze('maze.txt')
    a_star_path, a_star_backtrack = a_star(maze)
    plot_maze_with_path(maze, a_star_path, a_star_backtrack, "A*")

    write_paths_to_file(dfs_path, bfs_path, a_star_path)

if __name__ == "__main__":
    main()
