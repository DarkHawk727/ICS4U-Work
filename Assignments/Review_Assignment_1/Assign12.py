singer_a, singer_b, singer_c = 0, 0, 0
votes = list(str(input("Enter the votes: ")))

for vote in votes:
	if vote.upper() == "A":
		singer_a += 1
	elif vote.upper() == "B":
		singer_b += 1
	elif vote.upper() == "C": 
		singer_c += 1

# print(singer_a, singer_b, singer_c)

if singer_a == singer_b == singer_c:
	print("Singers A, B, C tied with {} votes".format(singer_a))

elif singer_a == singer_b and singer_a > singer_c:
	print("Singers A and B both tied with {} votes".format(singer_a))

elif singer_b == singer_c and singer_b > singer_a:
	print("Singers B and C both tied with {} votes".format(singer_b))

elif singer_a == singer_c and singer_a > singer_b:
	print("Singers A and C both tied with {} votes".format(singer_a))

elif max(singer_a, singer_b, singer_c) == singer_b:
	print("Singer B won with {} votes".format(singer_b))

elif max(singer_a, singer_b, singer_c) == singer_c:
	print("Singer C won with {} votes".format(singer_c))

elif max(singer_a, singer_b, singer_c) == singer_a:
	print("Singer A won with {} votes".format(singer_a))
