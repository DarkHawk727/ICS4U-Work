import numpy as np

file_number = str(input("Enter the file number: "))
filename = "Assignments/Recursion_Assignment_6/Part1/Sample_Files/Maze" + file_number + ".txt"

with open(filename, 'r') as file:
	raw_input = file.readline().split(",")
	x_dim, y_dim = int(raw_input[0]), int(raw_input[1])
# write code to read the file and store the maze in a 2D numpy array
	maze = np.empty((x_dim, y_dim), dtype=str)
	for i in range(x_dim):
		for j in range(y_dim):
			maze[i,j] = str(file.read(1))


print(x_dim, y_dim)
print(maze)
