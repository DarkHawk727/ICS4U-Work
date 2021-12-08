def calculate_patterns(previous_term, index, counter):
    if counter == index:
        return previous_term
    if counter % 2 == 0:
        return calculate_patterns(2 * previous_term + 3, index, counter + 1)
    else:
        return calculate_patterns(previous_term - 2, index, counter + 1)


initial_term = int(input("Please enter the initial term: "))
index = int(input("Please enter the index: ")) - 1
print(calculate_patterns(initial_term, index, 0))
