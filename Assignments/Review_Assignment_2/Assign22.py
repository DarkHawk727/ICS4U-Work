def merge_sort(grades):
	if len(grades) == 1:
		return grades
	else:
		midpoint = len(grades)//2
		left_half = grades[:midpoint]
		right_half = grades[midpoint:]

		merge_sort(left_half)
		merge_sort(right_half)      

		i = 0
		j = 0
		k = 0

		while i < len(left_half) and j < len(right_half):
			if left_half[i] < right_half[j]:
				grades[k] = left_half[i]
				i += 1
			else:
				grades[k] = right_half[j]
				j += 1
			k += 1
		
		while i < len(left_half):
			grades[k] = left_half[i]
			i += 1
			k += 1

		while j < len(right_half):
			grades[k] = right_half[j]
			j += 1
			k += 1

			return grades

# ========================================================================================================

class analyzer:
	def calculate_mean(grades):
		mean = sum(grades) / len(grades)
		return mean


	def find_median(grades):
		median_copy = grades.copy()
		median_marks = []
		n = len(median_copy)
		merge_sort(median_copy)

		if n % 2 == 0:
			median = (median_copy[n//2 - 1] + median_copy[n//2]) / 2
			median_marks.append(median_copy[n//2])
			median_marks.append(median_copy[n//2-1])
		else:
			median = median_copy[n//2]
			median_marks.append(median_copy[n//2])
		return median, median_marks


	def find_mode(grades):
		max_value = 0
		min_value = 0
		count_array = []

		for i in range(101):
			count_array.append(0)

		for element in grades:
			count_array[element] += 1
		
		for count in count_array:
			if count > max_value:
				max_value = count
			if count < min_value:
				min_value = count

		mode_indexes = [i for i, v in enumerate(count_array) if v == max_value and max_value != 1]

		return mode_indexes

# ========================================================================================================


grades, names = [], []

raw_input = "1"
while raw_input != "-1":
	raw_input = input("Please enter a student followed by a mark (seperated by a space): ")
	try:
		name = raw_input.split(" ")[0]
		grade = int(raw_input.split(" ")[1])
		if 0 <= grade <= 100:
			names.append(name)
			grades.append(grade)
		else:
			print("Grade is invalid!")
			raw_input = input("Please enter a student followed by a mark (seperated by a space): ")

	except IndexError as IE:
		pass

print("-"*100)
print("The average of the marks is: {:.1f}%".format(analyzer.calculate_mean(grades)))

print("-"*100)
median = analyzer.find_median(grades)[0]
print("The median mark is: {}%".format(median))
for i in range(len(grades)):
	for median_grade in analyzer.find_median(grades)[1]:
		if grades[i] == median_grade:
			print("{} has a median mark of {}%".format(names[i], median_grade))


print("-"*100)
modes = analyzer.find_mode(grades)
if not modes:
	print("There are no modes")
else:
	print("The mode(s) is/are: {}".format(", ".join(str(x)+"%" for x in analyzer.find_mode(grades))))
	for mode in modes:
		for i in range(len(grades)):
			if mode == grades[i]:
				print("{} recieved a mode mark of {}%".format(names[i], mode))
