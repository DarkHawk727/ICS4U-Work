def recursivley_find_longest_palindrome(input_text, i, inc, palindromes, size):
    if i > len(input_text):
        return palindromes
    j = i + inc
    if j <= len(input_text):
        if is_Palindrome(input_text[i:j]):
            if len(input_text[i:j]) > size:
                palindromes = input_text[i:j]
        return recursivley_find_longest_palindrome(input_text, i, inc+1, palindromes, len(palindromes))
    else:
        return recursivley_find_longest_palindrome(input_text, i+1, 1, palindromes, len(palindromes))


def is_Palindrome(input):
    temp_word = input.replace(' ', '').lower()
    word = temp_word[::-1]
    return word == temp_word


palindromes = ""
input_string = input("Enter a string: ")
print(recursivley_find_longest_palindrome(input_string, 0, 1, palindromes, 0))
