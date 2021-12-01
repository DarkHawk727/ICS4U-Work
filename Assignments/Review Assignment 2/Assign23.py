import numpy as np

board = np.zeros((8, 8), dtype=int)
won = False
player = 1

def print_board(board):
	for row in board:
			for column in row:
				print(column, end=" ")
			print()
	print("A B C D E F G H")
	print()


def place_piece(board, player, choice):
	if player == 1:
		print("Current player: 1")
		for i in range(7, -1, -1):
				if board[i, choice] == 0:
					board[i, choice] = 1
					break
	
	elif player == 2:
		print("Current player: 2")
		for i in range(7, -1, -1):
				if board[i, choice] == 0:
					board[i, choice] = 2
					break

# TODO: Add a function that checks if the board is full
# TODO: Finish the check_win function
def check_win(board, player):
	temp_bool = False
	win_count = 0
	temp_board = board.tolist()
	regular_v, upside_down_v = [], []
	print(temp_board)
	for row in range(6):
		for column in range(4):
			if temp_board[row][column] > 0:
				regular_v.append(temp_board[row][column])
				regular_v.append(temp_board[row][column+4])
				regular_v.append(temp_board[row+1][column+1])
				regular_v.append(temp_board[row+1][column+2])
				regular_v.append(temp_board[row+2][column+2])
				print(regular_v)
			
				if all(regular_v) == 1:
					temp_bool = True
				elif all(regular_v) == 2:
					temp_bool = True
			regular_v = []
				# if temp_board[row][column] == temp_board[row][column+4] == temp_board[row+1][column+1] == temp_board[row+1][column+2] == temp_board[row+2][column+2]:
	return temp_bool



while not won:
	print_board(board)
	raw_input = input("Please select a column (A-H): ")
	choice = ord(raw_input.lower()) - 97
	place_piece(board, player, choice)
	if check_win(board, player):
		print("Player " + str(player) + " wins!")
		won = True
	if np.all(board):
		print("Tie!")
		won = True
	player = 3 - player
