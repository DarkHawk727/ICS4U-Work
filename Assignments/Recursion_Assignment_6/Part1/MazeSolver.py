import numpy as np


def find_path(maze, x, y):
    if x < 0 or x >= x_dim or y < 0 or y >= y_dim:
        return False
    elif maze[x, y] == "x":
        return True
    elif maze[x, y] == "." or maze[x, y] == "e":
        maze[x, y] = "+"
        if (
            find_path(maze, x, y - 1)
            or find_path(maze, x, y + 1)
            or find_path(maze, x - 1, y)
            or find_path(maze, x + 1, y)
        ):
            return True
        maze[x, y] = "."
    return False


file_number = str(input("Enter the file number: "))
filename = (
    "ICS4U-Work/Assignments/Recursion_Assignment_6/Part1/Sample_Files/Maze"
    + file_number
    + ".txt"
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
maze[initial_x, initial_y] = "e"

for i in range(x_dim):
    for j in range(y_dim):
        print(" {} ".format(maze[i][j]), end="")
    print()