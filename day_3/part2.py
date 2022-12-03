from functools import reduce

with open("input") as f:
	lines = [line.strip() for line in f.readlines()]

priority_sum = 0

n = 3
groups = [lines[i: i + n] for i in range(0, len(lines), n)]

total_score = 0

for group in groups:
	sets = [set(c for c in items) for items in group]
	intersection = reduce(lambda x, y: x & y, sets).pop()

	if intersection.isupper():
		total_score += ord(intersection) - 38
	else:
		total_score += ord(intersection) - 96

print(total_score)
