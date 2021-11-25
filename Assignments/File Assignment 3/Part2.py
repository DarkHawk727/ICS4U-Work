n = int(input("Please enter the length of the lines: "))
text = open("Assignments/File Assignment 3/Accompanying Files/html_text.txt", 'r')
final_text = ""

for line in text.readlines():
    final_text += line.strip()

final_text = final_text.replace("<br>", "\n")
final_text = final_text.replace("<p>", "\n\n")
final_text = final_text.replace("<hr>", "-" * n)

print(final_text)
