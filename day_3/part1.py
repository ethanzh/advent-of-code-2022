with open("input") as f:
	lines = [line.strip() for line in f.readlines()]

priority_sum = 0

for rucksack_items in lines:
	length = len(rucksack_items)
	midpoint_index = length // 2
	halves = rucksack_items[:midpoint_index], rucksack_items[midpoint_index:]
	first_half = set(item for item in halves[0])
	second_half = set(item for item in halves[1])

	duplicate_item = first_half.intersection(second_half).pop()

	if duplicate_item.isupper():
		priority_sum += ord(duplicate_item) - 38
	else:
		priority_sum += ord(duplicate_item) - 96

print(priority_sum)
