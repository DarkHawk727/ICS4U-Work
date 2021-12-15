words = []
with open("Assignments/Binary_Search_Assignment/dictionary.txt", 'r') as dictionary:
	words.append(dictionary.read().strip())

words.sort()

def binary_search(arr, high, low, element):
	if high >= low:
		middle = (high+low) // 2

		if arr[middle] == element:
			return middle

		elif arr[mid] > element:
			return binary_search(arr, mid-1, low, element)
		
		else:
			return binary_search
				return binary_search(arr, mid+1, low, element)
	
	else:
		return -1

word = str(input("Please enter a string: "))

if binary_search(words, )