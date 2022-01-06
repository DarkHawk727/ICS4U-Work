import numpy as np


def find_path(maze, x, y):
    if x < 0 or x >= x_dim or y < 0 or y >= y_dim:
        return False
    elif maze[x, y] == "x":
        return True
    elif maze[x, y] == ".":
        maze[x, y] = "+"
        return (
            find_path(maze, x, y - 1)  # North
            or find_path(maze, x, y + 1)  # South
            or find_path(maze, x - 1, y)  # West
            or find_path(maze, x + 1, y)  # East
        )
    elif maze[x, y] == "+":
        maze[x, y] = "."
        return (
            find_path(maze, x, y - 1)  # North
            or find_path(maze, x, y + 1)  # South
            or find_path(maze, x - 1, y)  # West
            or find_path(maze, x + 1, y)  # East
        )
    return False


file_number = str(input("Enter the file number: "))
filename = (
    "Assignments/Recursion_Assignment_6/Part1/Sample_Files/Maze" + file_number + ".txt"
)

with open(filename, "r") as file:
    raw_input = file.readline().split(",")
    x_dim, y_dim = int(raw_input[0]), int(raw_input[1])

    maze = np.zeros((x_dim, y_dim), dtype=str)

    raw_input = file.readlines()

    for i in range(x_dim):
        for j in range(y_dim):
            maze[i, j] = list(raw_input[i])[j]

initial_x, initial_y = np.where(maze == "e")  # Find the starting point
print((find_path(maze, initial_x, initial_y)))
print(maze)
