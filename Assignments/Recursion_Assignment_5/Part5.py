<<<<<<< HEAD
def recursivley_find_longest_palindrome(input, i, inc, pals, size):
    if i > len(input):
        return pals
    j = i+inc
    if j <= len(input):
        if is_Palindrome(input[i:j]):
            if len(input[i:j]) > size:
                pals = input[i:j]
        return recursivley_find_longest_palindrome(input, i, inc+1, pals, len(pals))
    else:
        return recursivley_find_longest_palindrome(input, i+1, 1, pals, len(pals))


def is_Palindrome(input):
    tempWord = input.replace(' ', '').lower()
    word = tempWord[::-1]
    return word == tempWord


pals = ""
print(recursivley_find_longest_palindrome("Some like cake but I prefer pie", 0, 1, pals, 0))
=======
def recursivley_find_longest_palindrome(string, palindrome, start_index, end_index):
	 


def check_palindrome(string):
	if string.lower().replace(" ", "") == string[::-1].lower().replace(" ", ""):
		return True
	else:
		return False 


print(recursivley_find_longest_palindrome("Some like cake but I prefer pie"))
>>>>>>> ae857b8b29b93c6a2781996f2c67d0fc37d15a6a
