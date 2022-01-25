import numpy as np


def binary_search(arr, target):
    arr = sorted(arr)
    start, end = 0, len(arr) - 1

    while start <= end:
        middle = (start + end) // 2
        middle_element = arr[middle]

        if middle_element > target:
            end = middle - 1
        elif middle_element < target:
            start = middle + 1
        else:
            return middle_element


def find_words(arr, word):
    word = word.upper()
    for elem in arr:
        if elem.find(word) > -1 or elem[::-1].find(word) > -1:
            print('"{}" was found in the board.'.format(word.lower()))


dictionary_words = []
with open("ICS4U-Work/Assignments/Binary_Search_Assignment/Accompanying_Files/dictionary.txt","r",) as dictionary:
    for word in dictionary:
        dictionary_words.append(word.strip())

rows, columns, diagonals = [], [], []

with open("ICS4U-Work/Assignments/Binary_Search_Assignment/Accompanying_Files/grid.txt","r",) as f:
    grid = f.read().splitlines()
n = int(grid[0])
grid = grid[1:]
board = np.array([i for elem in grid for i in elem]).reshape(n, n)

[rows.append("".join(board[:, i])) for i in range(n)]

[columns.append("".join(board[i, :])) for i in range(n)]

diags = [board[::-1, :].diagonal(i) for i in range(-n + 1, n)]
diags.extend(board.diagonal(i) for i in range(n - 1, -n, -1))

[diagonals.append("".join(elem)) for elem in diags]

word = str(input("Please enter a word: ")).lower()

if binary_search(dictionary_words, word) is not None:
    print('"{}" is in the dictionary'.format(word))
    find_words(rows, word)
    find_words(columns, word)
    find_words(diagonals, word)
else:
    print('"{}" is NOT in the dictionary.'.format(word))
