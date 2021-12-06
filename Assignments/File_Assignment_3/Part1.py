words_list = []
word_frequency = {}

with open(
    "Assignments/File_Assignment_3/Accompanying_Files/sample_text.txt", "r"
) as text:
    for line in text.readlines():
        line = line.strip().lower()

        for punc in "!?\":;,()'.*[]{}":
            line = line.replace(punc, "")
        words_list = line.split(" ")

        for word in words_list:
            if not word:
                continue
            try:
                word_frequency[word] += 1
            except KeyError:
                word_frequency[word] = 1
sorted_frequency = sorted(word_frequency.items(), key=lambda item: item[0])

print("{:<25} {:>10}".format("WORD", "FREQUENCY"))
print("-" * 36)

for line in sorted_frequency:
    print("{:<25} {:>10}".format(line[0], line[1]))
print("-" * 36)
print("{:<25} {:>10}".format("TOTAL:", sum(word_frequency.values())))
