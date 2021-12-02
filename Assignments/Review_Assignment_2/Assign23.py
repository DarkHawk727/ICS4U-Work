import numpy as np

board = np.zeros((8, 8), dtype=int)

global won
global valid

def print_board(board):
	for row in board:
			for column in row:
				print(column, end=" ")
			print()
	print("A B C D E F G H")
	print()


def place_piece(board, player, choice):
	valid = False
	if choice < 8:
		if player == 1:
			print("Current player: 2")
			for i in range(7, -1, -1):
					if board[i, choice] == 0:
						board[i, choice] = 1
						valid = True
						break
		
		elif player == 2:
			print("Current player: 1")
			for i in range(7, -1, -1):
					if board[i, choice] == 0:
						board[i, choice] = 2
						valid = True
						break
	else:
		print("Invalid choice!")
		player = player
	return valid
		

def check_win(board, player):
	temp_board = board.tolist()
	bruh = False
	for column in range(7):
		for row in range(7):
			try:
				if temp_board[row][column] == temp_board[row+1][column+1] == temp_board[row+2][column+2] == temp_board[row+1][column+3] == temp_board[row][column+4] == player:
					bruh = True
			except IndexError as IE:
				pass
	for column in range(20):
		for row in range(20):
			try:
				if temp_board[row][column] == temp_board[row-1][column+1] == temp_board[row-2][column+2] == temp_board[row-1][column+3] == temp_board[row][column+4] == player:
					bruh = True
			except IndexError as IE:
				pass
	return bruh


won = False
player = 1

print("Current player: 1")
while not won:
	print_board(board)
	valid = False
	while not valid:
		raw_input = input("Please select a column (A-H): ")
		choice = ord(raw_input.lower()) - 97
		valid = place_piece(board, player, choice)
	won = check_win(board, player)
	player = 3 - player
	if np.sum(board) == 96:
		print_board(board)
		print("TIE")
		break

if won:
	print_board(board)
	print("Player ", 3-player, " has WON!")
