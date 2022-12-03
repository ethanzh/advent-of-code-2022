with open("input") as f:
	lines = f.readlines()

accumulator = 0
top_three = []

for line in lines:
	if line == "\n":
		if len(top_three) < 3:
			top_three.append(accumulator)
		elif accumulator > min(top_three):
			top_three.remove(min(top_three))
			top_three.append(accumulator)
		accumulator = 0
	else:
		value = int(line.replace("\n", ""))
		accumulator += value

print(sum(top_three))
