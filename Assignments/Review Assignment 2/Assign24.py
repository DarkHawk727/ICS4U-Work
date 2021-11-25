import numpy as np

scores = []

def merge_sort(scores):
		if len(scores) == 1:
			return scores
		else:
			midpoint = len(scores)//2
			left_half = scores[:midpoint]
			right_half = scores[midpoint:]

			merge_sort(left_half)
			merge_sort(right_half)      

			i = 0
			j = 0
			k = 0

			while i < len(left_half) and j < len(right_half):
				if left_half[i] < right_half[j]:
					scores[k] = left_half[i]
					i += 1
				else:
					scores[k] = right_half[j]
					j += 1
				k += 1
			
			while i < len(left_half):
				scores[k] = left_half[i]
				i += 1
				k += 1

			while j < len(right_half):
				scores[k] = right_half[j]
				j += 1
				k += 1

			return scores
	
print("Please enter the scores (Use -1 to indicate the end of the scores): ")
score = "1"
while score != "-1":
	score = input()
	scores.append(int(score))

scores.pop()

scores = merge_sort(scores)

n = len(scores)

score_board = np.zeros((n, n), dtype=int)


def calculate_differences(scores):
	for i in range(n-1):
		for j in range(n):
			score_board[i,j] = scores[j] - scores[i]
			if j <= i:
				score_board[i,j] = scores[j] - scores[i+1]
	return score_board


def print_board(scores, score_board, sums):
	for score in scores:
		print("{:>4}".format(score), end='')
	print()
	print('-' * (4*n))
	for row in range(len(score_board)-1):
		for column in range(len(score_board)):
			if score_board[row, column] >= 0:
				print("{:>4}".format(score_board[row,column]), end='')
			else:
				print("{:>4}".format(score_board[row,column]), end='')
		print()
	print('-' * (4*n))
	for element in sums:
		print("{:>4}".format(element), end='')


calculate_differences(scores)
sums = 	score_board.sum(axis=0)
print_board(scores, score_board, sums)
print()
