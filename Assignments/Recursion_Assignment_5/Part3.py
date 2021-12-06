def recursive_palindrome_checker(text):
    text = text.lower()
    if len(text) == 0:
        return True
    elif len(text) == 1:
        return True
    elif text[0] == text[-1]:
        return recursive_palindrome_checker(text[1:-1])
    else:
        return False


text = input("Enter a string: ")

if recursive_palindrome_checker(text):
    print("The string is a palindrome!")
else:
    print("The string is NOT a palindrome. :(")
