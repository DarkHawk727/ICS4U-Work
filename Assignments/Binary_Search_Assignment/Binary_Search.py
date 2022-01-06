import numpy as np

dictionary_words = []
with open("C:/Users/arjun/Desktop/School/Grade 12/Quadmester 2/ICS4U/ICS4U-Work/Assignments/Binary_Search_Assignment/dictionary.txt", 'r') as dictionary:
	dictionary_words.append(dictionary.read().strip())


def binary_search(arr, high, low, element):
	arr.sort()
	if high >= low:
		middle = (high+low) // 2

		if arr[middle] == element:
			return middle

		elif arr[middle] > element:
			return binary_search(arr, middle-1, low, element)
		else:
			return binary_search(arr, middle+1, low, element)
	
	else:
		return -1

# 1. User enters a word
# 2. Program checks if the word is in the dictionary using binary search
# 3. Program checks if the word is in the board

# Find the word in the board
def find_words(arr, words):
    for elem in arr:
        try:
            if elem.find(word) > -1 or elem[::-1].find(word) > -1:
                print("{} was found in the board".format(word))
                words.remove(word)
        except ValueError:
            pass


word = str(input("Please enter a word: "))
if binary_search(dictionary_words, len(dictionary_words), 0, word) > -1:
	print("{} is in the dictionary".format(word))
else:
	print("{} is not in the dictionary".format(word))

rows, columns, diagonals = [], [], []

with open("C:/Users/arjun/Desktop/School/Grade 12/Quadmester 2/ICS4U/ICS4U-Work/Assignments/File Assignment 3/Accompanying Files/grid.txt", "r") as f:
    grid = f.read().splitlines()
n = int(grid[0])
grid = grid[1:]
board = np.array([i for elem in grid for i in elem]).reshape(n, n)

[rows.append("".join(board[:, i])) for i in range(n)]

[columns.append("".join(board[i, :])) for i in range(n)]

# Create the diagonals using np.diagonal() and some clever indexing
diags = [board[::-1, :].diagonal(i) for i in range(-n + 1, n)]
diags.extend(board.diagonal(i) for i in range(n - 1, -n, -1))

[diagonals.append("".join(elem)) for elem in diags]

find_words(rows, word)
find_words(columns, word)
find_words(diagonals, word)
