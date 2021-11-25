text = open("Assignments/File Assignment 3/Accompanying Files/sample_text.txt", 'r')
words_list = []
word_frequency = {}

for line in text.readlines():
	line = line.strip().lower()

	for punc in "!?\":;,()\'.*[]{}":
		line = line.replace(punc, "")

	words_list = line.split(" ")

	for word in words_list:
		if not word:
			continue
		try:
			word_frequency[word] += 1
		except KeyError:
			word_frequency[word] = 1

# Create your own sorting algo
sorted_frequency = sorted(word_frequency.items(), key=lambda item: item[1], reverse=True)

print("{:<25} {:>10}".format("WORD", "FREQUENCY"))
print("-"*36)

for line in sorted_frequency:
	print("{:<25} {:>10}".format(line[0], line[1]))

print("-"*36)
print("{:<25} {:>10}".format("TOTAL:", sum(word_frequency.values())))