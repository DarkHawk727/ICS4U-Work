final_text = ""

with open("Assignments/File_Assignment_3/Accompanying_Files/html_text.txt") as raw_text:
    for line in raw_text.readlines():
        final_text += line.strip()
    final_text = final_text.replace("<br>", "\n")
    final_text = final_text.replace("<p>", "\n\n")
    final_text = final_text.replace("<hr>", "-" * 35)
print(final_text)
