with open("input") as f:
	lines = f.readlines()

accumulator = 0
max_value = 0

for line in lines:
	if line == "\n":
		if accumulator > max_value:
			max_value = accumulator
		accumulator = 0
	else:
		value = int(line.replace("\n", ""))
		accumulator += value

print(max_value)
