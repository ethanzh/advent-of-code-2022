with open("input") as f:
	lines = f.readlines()
	

SHAPE_SCORE_MAP = {
	"X": 1,
	"Y": 2,
	"Z": 3
}

# [us][opponent]
RESULT_MATRIX = [
	[3,0,6],
	[6,3,0],
	[0,6,3]
]

SHAPE_INDEX_MAP = {
	"A": 0,
	"B": 1,
	"C": 2,
	"X": 0,
	"Y": 1,
	"Z": 2
}

total_score = 0

for line in lines:
	line = line.strip()
	opponent, us = line.split()
	total_score += RESULT_MATRIX[SHAPE_INDEX_MAP[us]][SHAPE_INDEX_MAP[opponent]]
	total_score += SHAPE_SCORE_MAP[us]
	
print(total_score)
