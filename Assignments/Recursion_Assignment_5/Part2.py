def recursive_find_digit_sum(number):
    # Base Case: if the number is only 1 digit then the sum is just that digit.
	if number < 10:
        return number
    else:
        return number % 10 + recursive_find_digit_sum(number // 10)


n = int(input("Enter a number: "))
print("The sum of the digits of the number is: {}".format(recursive_find_digit_sum(n)))
