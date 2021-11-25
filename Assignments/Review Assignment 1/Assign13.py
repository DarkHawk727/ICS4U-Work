def scale_icon(k):
	for i in range(k):
			print("*"*k + "X"*k + "*"*k)

	for i in range(k):
			print("X"*k + "*"*k + "*"*k)

	for i in range(k):
			print("*"*k + "*"*k + "X"*k)

scaling_factor = int(input("Please enter a scaling factor: "))

scale_icon(scaling_factor)