"""
+---------------+
|Rushi Shah		|
|12/25/14		|
|Sudoku solver	|
|AI 6th period	|
+---------------+
"""

from copy import deepcopy
MAX = 9

#Setup
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
		if(self.value == {1, 2, 3, 4, 5, 6, 7, 8, 9}):
			return "{0}"
		if(len(self.value)>1):
			return "{0}"
		return str(self.value)

def blocks(matrix):
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

	return block

def displayTheBoard(matrix):
	for i in range(MAX):
		for j in range(MAX):
			print(matrix[i][j], end = " ")
		print()
	print("-"*35)

def solutionIsCorrect(matrix):
	rows = [[] for x in range(MAX)]
	cols = [[] for x in range(MAX)]
	for r in range(MAX):
		for c in range(MAX):
			rows[r].append(matrix[r][c].value)
			cols[c].append(matrix[r][c].value)

	block = blocks(matrix)

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

def createMatrix():
	M = [
		[8, 1, 2, 0, 0, 0, 0, 0, 9,], 
		[9, 4, 3, 0, 0, 0, 0, 0, 5,],
		[6, 7, 5, 0, 0, 0, 0, 0, 3,], 
		[1, 5, 4, 0, 0, 0, 0, 0, 6,], 
		[3, 6, 9, 0, 0, 0, 0, 0, 1,], 
		[2, 8, 7, 0, 0, 0, 0, 0, 4,], 
		[5, 2, 1, 9, 7, 4, 3, 6, 8,], 
		[4, 3, 8, 5, 2, 6, 9, 1, 7,],
		[7, 9, 6, 3, 1, 8, 4, 5, 2,]
	]
	matrix = []
	for r in range(MAX):
		row = []
		for c in range(MAX):
			row.append(Cell(M[r][c], r, c, matrix))
		matrix.append(row)
	return matrix

#Tricks one and two
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
						#print("increasing depth")
						makeAllPossibleSimpleChangesToMatrix(matrix)
	#print("returning")
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
						#print("increasing depth")
						makeAllPossibleSimpleChangesToMatrix(matrix)
	#print("returning")
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
						#print("increasing depth")
						makeAllPossibleSimpleChangesToMatrix(matrix)
	#print('returning')
	return matrix

def trick2Row(matrix):
	for r in range(MAX):
		possibilities = [x+1 for x in range(MAX)]
		for possibility in possibilities:
			indices = []
			for c in range(MAX):
				if(len(matrix[r][c].value)>1):
					if(possibility in matrix[r][c].value):
						indices.append(c)
			if(len(indices) == 1):
				matrix[r][indices[0]].value = {possibility}
				return recursivelySolveTheSudoku(matrix)
	return matrix

def trick2Col(matrix):
	for c in range(MAX):
		possibilities = [x+1 for x in range(MAX)]
		for possibility in possibilities:
			indices = []
			for r in range(MAX):
				if(len(matrix[r][c].value)>1):
					if(possibility in matrix[r][c].value):
						indices.append(r)
			if(len(indices) == 1):
				matrix[indices[0]][c].value = {possibility}
				return recursivelySolveTheSudoku(matrix)
	return matrix

def trick2Block(matrix):
	for i in range(MAX):
		#inside a block from now on
		possibilities = [x+1 for x in range(MAX)]
		for possibility in possibilities:
			found = 0
			for r in range(MAX):
				for c in range(MAX):
					if(i == matrix[r][c].blockNumber()):
						if(len(matrix[r][c].value) >1 and possibility in matrix[r][c].value):
							found+=1
			if(found == 1):
				for r in range(MAX):
					for c in range(MAX):
						if(i == matrix[r][c].blockNumber()):
							if(possibility in matrix[r][c].value):
								matrix[r][c].value = {possibility}
								return recursivelySolveTheSudoku(matrix)
	return matrix

def makeAllPossibleSimpleChangesToMatrix(matrix):
	#trick 1
	matrix = rowChanges(matrix)
	matrix = colChanges(matrix)
	matrix = blockChanges(matrix)
	
	#trick 2
	matrix = trick2Row(matrix)
	matrix = trick2Col(matrix)
	matrix = trick2Block(matrix)

	return matrix

def badMatrix(matrix):
	for r in range(MAX):
		for c in range(MAX):
			if matrix[r][c].value == set(): #empty
				return True
	return False

def restoreValue(matrix, oldMatrix):
	for r in range(MAX):
		for c in range(MAX):
			matrix[r][c].value = oldMatrix[r][c].value
	return matrix

def coordinatesOfCellWithSmallestValueSet(matrix):
	currMin = 11
	currFound = False
	for r in range(MAX):
		for c in range(MAX):
			if(1 < len(matrix[r][c].value) < currMin):
				currMin = len(matrix[r][c].value)
				currCoords = (r, c)
				currFound = True
	if(currFound):
		return currCoords
def isFilled(matrix):
	for r in range(MAX):
		for c in range(MAX):
			if(len(matrix[r][c].value) > 1):
				return False
	return True

def recursivelySolveTheSudoku(matrix):
	#Trick 1 and 2
	matrix = makeAllPossibleSimpleChangesToMatrix(matrix)
	if(solutionIsCorrect(matrix)):
		return matrix
	elif(badMatrix(matrix) or isFilled(matrix)):
		return matrix #return it anyways to unwind the bad matrix
	#Trick 3
	oldMatrix = deepcopy(matrix)
	r, c = coordinatesOfCellWithSmallestValueSet(matrix)
	#print("Calculated coordinates of cell with smallest set:", r, c)
	#for loop for each guess
	guesses = matrix[r][c].value
	#print("Possible guesses are", guesses)
	for guess in guesses:
		matrix[r][c].value = {guess}
		#print("Inserting", guess, "into", r, c)
		matrix = recursivelySolveTheSudoku(matrix)
		if(solutionIsCorrect(matrix)):
			return matrix
		else:
			#print("Restoring values")
			matrix = restoreValue(matrix, oldMatrix)
	return matrix

def main():
	matrix = createMatrix()
	displayTheBoard(matrix)
	matrix = recursivelySolveTheSudoku(matrix)
	displayTheBoard(matrix)
	if(solutionIsCorrect(matrix)):
		print("Matrix is correct")
	elif(badMatrix(matrix)):
		print("Bad matrix")
	else:
		print("Unable to solve")

main()