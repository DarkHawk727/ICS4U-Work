import numpy as np

words, rows, columns, diagonals = [], [], [], []

# Function that checks word against element of array and its reverse.
def find_words(arr, words):
    for elem in arr:
        for word in words:
            try:
                if elem.find(word) > -1 or elem[::-1].find(word) > -1:
                    print("{} was found in the board".format(word))
                    words.remove(word)
            except ValueError:
                pass


with open("Assignments/File Assignment 3/Accompanying Files/words.txt", "r") as f:
    words = f.read().splitlines()
with open("Assignments/File Assignment 3/Accompanying Files/grid.txt", "r") as f:
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

find_words(rows, words)
find_words(columns, words)
find_words(diagonals, words)

[print("{} was NOT found in the board".format(word)) for word in words]
