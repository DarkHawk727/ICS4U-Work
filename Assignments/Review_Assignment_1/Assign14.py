from numpy import random

nums = []
big_num = ""
x_num = 0
# Example number: 3145122112381829

while len(set(nums)) < 10:
    nums = random.randint(50, size=(10))
print("The randomly generated numbers are: {}".format(nums))

for number in nums:
    big_num += str(number)
print("The concatenated number is: {}".format(big_num))

print("Every second digit is:")
for digit in big_num[::2]:
    print(digit)

x_num = sum([int(x) for x in list(big_num[::2])])

print("Coder X's number is: {}".format(x_num))
