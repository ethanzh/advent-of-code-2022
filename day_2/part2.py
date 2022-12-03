with open("input") as f:
	lines = f.readlines()
	

SHAPE_SCORE_MAP = {
	"X": 0,
	"Y": 3,
	"Z": 6
}

SHAPE_INDEX_MAP = {
	"A": 0,
	"B": 1,
	"C": 2,
	"X": 0,
	"Y": 1,
	"Z": 2
}

# [result {lose, draw, win}][opponent {rock, paper, scissors}]
RESULT_MATRIX = [
	[3, 1, 2],
	[1, 2, 3],
	[2, 3, 1]
]

total_score = 0

for line in lines:
	line = line.strip()
	opponent, result = line.split()
	our_choice = RESULT_MATRIX[SHAPE_INDEX_MAP[result]][SHAPE_INDEX_MAP[opponent]]
	result = SHAPE_SCORE_MAP[result]
	total_score += (our_choice + result)
	
	
print(total_score)
