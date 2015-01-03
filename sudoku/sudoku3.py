from copy import deepcopy
MAX = 9
class Cell(object):
	matrix = None
	def __init__(self, val, r, c, matrix):
		if val != 0:
			self.value = {val, }
		else:
			self.value = {1, 2, 3, 4, 5, 6, 7, 8, 9, }
		self.row = r
		self.col = c
		self.block = self.blockNumber()
		Cell.matrix = matrix
	def blockNumber(self):
		if((self.row < 3) 		and (self.col < 3)): 		return 0
		if((self.row < 3) 		and (2 < self.col < 6)): 	return 1
		if((self.row < 3) 		and (5 < self.col)): 		return 2
		if((2 < self.row < 6) 	and (self.col < 3)): 		return 3
		if((2 < self.row < 6) 	and (2 < self.col < 6)): 	return 4
		if((2 < self.row < 6) 	and (5 < self.col)):		return 5
		if((self.row > 5) 		and (self.col < 3)): 		return 6
		if((self.row > 5) 		and (2 < self.col < 6)): 	return 7
		if((self.row > 5)		and (5 < self.col)):		return 8
	def __repr__(self):
		# if(self.value == {1, 2, 3, 4, 5, 6, 7, 8, 9}):
		# 	return "{0}"
		return str(self.value)
		


def solutionIsCorrect(matrix):
	rows = [[] for x in range(MAX)]
	cols = [[] for x in range(MAX)]
	for r in range(MAX):
		for c in range(MAX):
			rows[r].append(matrix[r][c].value)
			cols[c].append(matrix[r][c].value)

	block = [[] for x in range(MAX)]

	block[0] = [
		matrix[0][0].value, matrix[0][1].value, matrix[0][2].value, 
		matrix[1][0].value, matrix[1][1].value, matrix[1][2].value,
		matrix[2][0].value, matrix[2][1].value, matrix[2][2].value 
	]
	block[1] = [
		matrix[0][3].value, matrix[0][4].value, matrix[0][5].value, 
		matrix[1][3].value, matrix[1][4].value, matrix[1][5].value,
		matrix[2][3].value, matrix[2][4].value, matrix[2][5].value 
	]
	block[2] = [
		matrix[0][6].value, matrix[0][7].value, matrix[0][8].value, 
		matrix[1][6].value, matrix[1][7].value, matrix[1][8].value,
		matrix[2][6].value, matrix[2][7].value, matrix[2][8].value 
	]

	block[3] = [
		matrix[3][0].value, matrix[3][1].value, matrix[3][2].value, 
		matrix[4][0].value, matrix[4][1].value, matrix[4][2].value,
		matrix[5][0].value, matrix[5][1].value, matrix[5][2].value 
	]
	block[4] = [
		matrix[3][3].value, matrix[3][4].value, matrix[3][5].value, 
		matrix[4][3].value, matrix[4][4].value, matrix[4][5].value,
		matrix[5][3].value, matrix[5][4].value, matrix[5][5].value 
	]
	block[5] = [
		matrix[3][6].value, matrix[3][7].value, matrix[3][8].value, 
		matrix[4][6].value, matrix[4][7].value, matrix[4][8].value,
		matrix[5][6].value, matrix[5][7].value, matrix[5][8].value 
	]

	block[6] = [
		matrix[6][0].value, matrix[6][1].value, matrix[6][2].value, 
		matrix[7][0].value, matrix[7][1].value, matrix[7][2].value,
		matrix[8][0].value, matrix[8][1].value, matrix[8][2].value 
	]
	block[7] = [
		matrix[6][3].value, matrix[6][4].value, matrix[6][5].value, 
		matrix[7][3].value, matrix[7][4].value, matrix[7][5].value,
		matrix[8][3].value, matrix[8][4].value, matrix[8][5].value 
	]
	block[8] = [
		matrix[6][6].value, matrix[6][7].value, matrix[6][8].value, 
		matrix[7][6].value, matrix[7][7].value, matrix[7][8].value,
		matrix[8][6].value, matrix[8][7].value, matrix[8][8].value 
	]

	for r in rows:
		for n in range(1, MAX+1):
			if{n} not in r:
				return False
	for c in cols:
		for n in range(1, MAX+1):
			if {n} not in c:
				return False
	for b in block:
		for n in range(1, MAX+1):
			if{n} not in b:
				return False
	return True

def badMatrix(matrix):
	for r in range(MAX):
		for c in range(MAX):
			if matrix[r][c].value == set(): #empty
				return True
	return False

def createMatrix():
	M = [
		[4,8,3,9,2,1,6,5,7],
		[9,6,7,3,4,5,8,2,1],
		[2,5,1,8,7,6,4,9,3],
		[0,0,0,0,3,2,9,7,6],
		[0,0,0,0,6,4,1,3,8],
		[0,0,0,0,9,8,2,4,5],
		[3,7,2,6,8,9,5,1,4],
		[8,1,4,2,5,3,7,6,9],
		[6,9,5,4,1,7,3,8,2]
	]
	matrix = []
	for r in range(MAX):
		row = []
		for c in range(MAX):
			row.append(Cell(M[r][c], r, c, matrix))
		matrix.append(row)
	return matrix
def restoreValue(matrix, oldMatrix):
	for r in range(MAX):
		for c in range(MAX):
			matrix[r][c].value = oldMatrix[r][c].value
	return matrix


def rowChanges(matrix):
	# check cells row
	for r in range(MAX):
		for c in range(MAX):
			toSubtract = set()
			if(len(matrix[r][c].value) > 1):
				for col in range(MAX):
					if(len(matrix[r][col].value) == 1):
						toSubtract = toSubtract | matrix[r][col].value
				if(len(toSubtract) > 0):
					matrix[r][c].value -= toSubtract
					if(len(matrix[r][c].value) == 1):
						print("increasing depth")
						makeAllPossibleSimpleChangesToMatrix(matrix)
	print("returning")
	return matrix
def colChanges(matrix):
	# check cells column
	for r in range(MAX):
		for c in range(MAX):
			toSubtract = set()
			if(len(matrix[r][c].value) > 1):
				for row in range(MAX):
					if(len(matrix[row][c].value) == 1):
						toSubtract = toSubtract | matrix[row][c].value
				if(len(toSubtract) > 0):
					matrix[r][c].value -= toSubtract
					if(len(matrix[r][c].value) == 1):
						print("increasing depth")
						makeAllPossibleSimpleChangesToMatrix(matrix)
	print("returning")
	return matrix
def blockChanges(matrix):
	for r in range(MAX):
		for c in range(MAX):
			toSubtract = set()
			if(len(matrix[r][c].value) > 1):
				for row in range(MAX):
					for col in range(MAX):
						if(len(matrix[row][col].value) == 1 and matrix[row][col].blockNumber() == matrix[r][c].blockNumber()):
							toSubtract = toSubtract | matrix[row][col].value 
				if(len(toSubtract) > 0):
					matrix[r][c].value -= toSubtract
					if(len(matrix[r][c].value) == 0):
						print("increasing depth")
						makeAllPossibleSimpleChangesToMatrix(matrix)
	print('returning')
	return matrix
def makeAllPossibleSimpleChangesToMatrix(matrix):
	#before = deepcopy(matrix)
	matrix = rowChanges(matrix)
	matrix = colChanges(matrix)
	matrix = blockChanges(matrix)
	# if(before != matrix):
	# 	matrix = makeAllPossibleSimpleChangesToMatrix(matrix)
	return matrix

def recursivelySolveTheSudoku(matrix):
	matrix = makeAllPossibleSimpleChangesToMatrix(matrix)
	return matrix
	if badMatrix(matrix) or solutionIsCorrect(matrix):
		return matrix
	oldMatrix = deepcopy(matrix)
	r, c = coordinatesOfCellWithSmallestValueSet(matrix)
	for guess in matrix[r][c].value:
		matrix[r][c].value = {guess,}
		matrix = recursivelySolveTheSudoku(matrix)
		if solutionIsCorrect(matrix):
			return matrix
		matrix = restoreValues(matrix, oldMatrix)
	return matrix
def displayTheBoard(matrix):
	for i in range(MAX):
		for j in range(MAX):
			print(matrix[i][j], end = " ")
		print()
	print("-"*35)

def main():
	matrix = createMatrix()
	displayTheBoard(matrix)
	matrix = recursivelySolveTheSudoku(matrix)
	displayTheBoard(matrix)
	print(solutionIsCorrect(matrix))
main()