
text = input("Please enter the text: ").split(" ")

for word in text:
    n = len(word)
    reverse = word[::-1]

    for i in range(n):
        print(" " * (n - i) + word[0:i].upper() +
              reverse[n - i + 1:n].upper())

    for i in range(n):
        print(" " * i + word[0:n - i].upper() + reverse[i + 1:n].upper())

    for i in range(1, n):
        print(" " * (n - 1) + word[i].upper())

    print()
