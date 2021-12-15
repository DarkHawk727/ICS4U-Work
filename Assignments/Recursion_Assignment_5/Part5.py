def recursivley_find_longest_palindrome(string, palindrome, start_index, end_index):
	 


def check_palindrome(string):
	if string.lower().replace(" ", "") == string[::-1].lower().replace(" ", ""):
		return True
	else:
		return False 


print(recursivley_find_longest_palindrome("Some like cake but I prefer pie"))
