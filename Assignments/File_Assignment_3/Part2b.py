n = int(input("Please enter the display line width: "))
final_text = ""

with open("Assignments/File_Assignment_3/Accompanying_Files/html_text.txt") as raw_text:
    for line in raw_text.readlines():
        final_text += line.strip()
    final_text = final_text.replace("<br>", "\n")
    final_text = final_text.replace("<p>", "\n\n")
    final_text = final_text.replace("<hr>", "-" * n)


lines = final_text.split("\n")
output = ""
for i in range(len(lines)):
	line = lines[i]
	while len(line) > n:
		end = line[:n]
		last_space = end.rfind(" ")
		first_space = line.find(" ")

		if last_space > -1:
			output += line[:last_space] + "\n"
			line = line[last_space+1:]
		elif first_space > -1:
			output += line[:first_space] + "\n"
			line = line[first_space+1:]
		else:
			output += line
			line = ""
	
	output += line
	output += "\n"

print(output)
