def calculate_patterns(previous_term, index, counter):
	if counter == previous_term:
		return previous_term
	
	if index % 2 != 0:
		counter += 1
		previous_term *= 2
		previous_term += 3
		return calculate_patterns(previous_term, index, counter)
	else:
		counter += 1
		previous_term -= 2
		return calculate_patterns(previous_term, index, counter)
	return calculate_patterns(previous_term, index, counter)

		
initial_term = int(input("Please enter the initial term: "))
index = int(input("Please enter the index: "))
print(calculate_patterns(initial_term, index, index), end=', ')
