import numpy as np

with open("Assignments/Recursion_Assignment_6/Part1/Sample_Files/File1.txt", 'r') as file:
	raw_input = file.readline().split(",")
	x_dim, y_dim = int(raw_input[0]), int(raw_input[1])
	maze = np.array([list(char) for char in file.readlines()])

print(x_dim, y_dim)
print(maze)