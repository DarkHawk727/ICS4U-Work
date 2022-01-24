names = list(input("Please enter a list of names seperated by a single space: ").split(" "))
num_turns = int(input("Please enter the number of turns: "))

while len(names) > 1:
    for _ in range(num_turns):
        names.append(names.pop(0))
    print("{} was eliminated".format(names.pop(0)))
    print("The remaining players are: {}".format([name for name in names]))
print("The winner is {}".format([name for name in names]))
