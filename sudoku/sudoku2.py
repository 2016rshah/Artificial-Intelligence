from copy import deepcopy
ROWS = 9
COLS = 9
# M = [
#     [4, 8, 1, 5, 0, 9, 6, 7, 0],
#     [3, 0, 0, 8, 1, 6, 0, 0, 2],
#     [5, 0, 0, 7, 0, 3, 0, 0, 8],
#     [2, 0, 0, 0, 0, 0, 0, 0, 9],
#     [9, 0, 0, 0, 0, 0, 0, 0, 1],
#     [8, 0, 0, 0, 0, 0, 0, 0, 4],
#     [0, 3, 9, 2, 7, 5, 4, 8, 0],
#     [6, 0, 0, 0, 0, 0, 9, 2, 7],
#     [7, 0, 0, 0, 0, 0, 3, 1, 0]
# ]
# M = [
# 	[0,2,6,1,8,0,3,0,0],
# 	[4,8,0,5,0,0,6,9,0],
# 	[0,5,0,9,7,2,8,1,0],
# 	[8,4,0,2,0,0,1,0,6],
# 	[2,0,0,6,1,8,0,0,3],
# 	[0,1,9,0,4,0,0,2,8],
# 	[5,0,8,0,7,1,0,0,9],
# 	[7,0,2,0,0,9,0,8,1],
# 	[0,0,4,0,2,6,7,3,0]
# ]
# SOLVED = [
# 	[4,8,3,9,2,1,6,5,7],
# 	[9,6,7,3,4,5,8,2,1],
# 	[2,5,1,8,7,6,4,9,3],
# 	[5,4,8,1,3,2,9,7,6],
# 	[7,2,9,5,6,4,1,3,8],
# 	[1,3,6,7,9,8,2,4,5],
# 	[3,7,2,6,8,9,5,1,4],
# 	[8,1,4,2,5,3,7,6,9],
# 	[6,9,5,4,1,7,3,8,2]
# ]
M = [
	[0,0,0,9,2,1,6,5,7],
	[0,0,0,3,4,5,0,2,0],
	[0,5,0,0,7,6,0,0,0],
	[5,0,8,0,3,2,0,7,6],
	[7,0,9,0,0,0,1,3,8],
	[0,0,6,7,0,0,2,0,0],
	[3,7,2,0,8,9,0,1,4],
	[8,1,4,2,5,0,7,6,0],
	[6,9,5,4,1,7,3,0,0]
]
class Cell(object):
	matrix = None
	def __init__(self, val, r, c, matrix):
		if(val != 0):
			self.value = {val,}
		else:
			self.value = {1, 2, 3, 4, 5, 6, 7, 8, 9,}
		self.row = r
		self.col = c
		self.block = self.blockNumber(r, c)
		Cell.matrix = matrix
	def blockNumber(self, r, c):
		if(r<=2):
			if(c<=2):
				return 0
			elif(c<=5):
				return 1
			elif(c<=8):
				return 2
		elif(r<=5):
			if(c<=2):
				return 3
			elif(c<=5):
				return 4
			elif(c<=8):
				return 5
		elif(r<=8):
			if(c<=2):
				return 6
			elif(c<=5):
				return 7
			elif(c<=8):
				return 8
	def __repr__(self):
		# if(self.value == {1, 2, 3, 4, 5, 6, 7, 8, 9}): return str({0})
		# else: return str(self.value)
		return str(self.value)
def printMatrix(m):
	print("[")
	for row in range(len(m)):
		print("  ", m[row])
	print("]")
def verifyBox(m, row, col):
	needed = [x for x in range(1, 10)]
	for i in range(-1, 2):
		for j in range(-1, 2):
			if(m[row+i][col+j] in needed):
				needed.pop(needed.index(m[row+i][col+j]))
			else:
				return False
	if(not needed):
		return True
	else:
		return False

def verifyTable(m):
	#check columns
	for i in range(len(m)):
		needed = [x for x in range(1, 10)]
		for j in range(len(m[i])):
			if(m[i][j] in needed):
				needed.pop(needed.index(m[i][j]))
			elif(m[i][j] == 0):
				return False
		if(needed):
			return False
	#check rows
	for col in range(len(m[0])):
		needed = [x for x in range(1, 10)]
		for row in range(len(m)):
			if(m[row][col] in needed):
				needed.pop(needed.index(m[row][col]))
			elif(m[row][col] == 0):
				return False
		if(needed):
			return False
	#check boxes
	for i in (1, 4, 7):
		for j in (1, 4, 7):
			if(not verifyBox(m, i, j)):
				return False

	#passed tests, return True
	return True
def fillRows(M):
	m = deepcopy(M)
	lowestNeeded = [x for x in range(1, 10)]
	for i in range(len(m)):
		needed = [x for x in range(1, 10)]
		emptyIndices = []
		for j in range(len(m[i])):
			if(m[i][j] in needed):
				needed.pop(needed.index(m[i][j]))
			elif(m[i][j] == 0):
				emptyIndices.append(j)
		if(len(needed) == 1 and len(emptyIndices) == 1):
			m[i][emptyIndices[0]] = needed[0]
		elif(len(needed)>1 and len(needed)<len(lowestNeeded)):
			lowestNeeded = needed
	if(m!=M):
		return m
	elif(len(lowestNeeded)!=10):
		return len(lowestNeeded)
	else:
		return -1
def fillCols(M):
	m = deepcopy(M)
	lowestNeeded = [x for x in range(1, 10)]
	for col in range(len(m[0])):
		needed = [x for x in range(1, 10)]
		emptyIndices = []
		for row in range(len(m)):
			if(m[row][col] in needed):
				needed.pop(needed.index(m[row][col]))
			elif(m[row][col] == 0):
				emptyIndices.append(row)
		if(len(needed) == 1 and len(emptyIndices) == 1):
			m[emptyIndices[0]][col] = needed[0]
		elif(len(needed)>1 and len(needed)<len(lowestNeeded)):
			lowestNeeded = deepcopy(needed)
	if(m!=M):
		return m
	elif(len(lowestNeeded) != 10):
		return len(lowestNeeded)
	else:
		return -1
def fillBoxes(M):
	m = deepcopy(M)
	lowestNeeded = [x for x in range(1, 10)]
	for ci in (1, 4, 7):
		for cj in (1, 4, 7):
			#center of box is m[ci][cj]
			needed = [x for x in range(1, 10)]
			emptyIndices = []
			for mi in (-1, 0, 1):
				for mj in (-1, 0, 1):
					i = ci+mi
					j = cj+mj
					if(m[i][j] in needed):
						needed.pop(needed.index(m[i][j]))
					elif(m[i][j] == 0):
						emptyIndices.append([i, j])
			if(len(needed) == 1 and len(emptyIndices) == 1):
				m[emptyIndices[0][0]][emptyIndices[0][1]] = needed[0]
			elif(len(needed)>1 and len(needed)<len(lowestNeeded)):
				lowestNeeded = deepcopy(needed)
	if(m!=M):
		return m
	elif(len(lowestNeeded)!=10):
		return len(lowestNeeded)
	else:
		return -1
def makeSimpleChanges(M):
	m = deepcopy(M)
	lowestNeeded = 10
	x = fillRows(m)
	if(type(x) is list): m = makeSimpleChanges(x)
	elif(x!=-1 and x<lowestNeeded): lowestNeeded = x 

	x = fillCols(m)
	if(type(x) is list): m = makeSimpleChanges(x)
	elif(x!=-1 and x<lowestNeeded): lowestNeeded = x 

	x = fillBoxes(m)
	if(type(x) is list): m = makeSimpleChanges(x)
	elif(x!=-1 and x<lowestNeeded): lowestNeeded = x 

	return m
def createMatrixObject(M):
	matrix = []
	for r in range(9):
		row = []
		for c in range(9):
			row.append(Cell(M[r][c], r, c, matrix))
		matrix.append(row)
	return matrix
def candidates(MO):
	mo = deepcopy(MO)
	for row in range(len(mo)):
		for col in range(len(mo[row])):
			candidates = mo[row][col].value
			if(len(candidates)>1):
				remSet = set()
				for i in range(len(mo)):
					if(len(mo[i][col].value) == 1):
						temp = mo[i][col].value.pop()
						mo[i][col].value.add(temp)
						remSet.add(temp)
				for j in range(len(mo)):
					if(len(mo[row][j].value) == 1):
						temp = mo[row][j].value.pop()
						mo[row][j].value.add(temp)
						remSet.add(temp)
				i = 0; j = 0;
				for i in range(len(mo)):
					for j in range(len(mo)):
						if(len(mo[i][j].value) == 1 and mo[i][j].block == mo[row][col].block):
							temp = mo[i][j].value.pop()
							mo[i][j].value.add(temp)
							remSet.add(temp)
				candidates = candidates - remSet
				mo[row][col].value = candidates
	return mo

def printMatrixObject(MO):
	for row in range(len(MO)):
		s = ""
		for col in range(len(MO[row])):
			s+=str((MO[row][col].value))
		print(s)
def convertMOtoM(MO):
	mo = deepcopy(MO)
	res = []
	for i in range(len(mo)):
		res.append([])
		for j in range(len(mo[i])):
			res[i].append(0)
			if(len(mo[i][j].value) == 1):
				res[i][j] = mo[i][j].value.pop()
	return res
def coordinatesOfCellWithSmallestValueSet(MO):
	mo = deepcopy(MO)
	smallest = 20
	coords = [-1, -1]
	for i in range(len(mo)):
		for j in range(len(mo[i])):
			if(len(mo[i][j].value) > 1 and len(mo[i][j].value) < smallest):
				smallest = len(mo[i][j].value)
				coords = [i, j]
	if(coords[0]!=-1):
		return coords
def revert(MO, oldMO):
	for r in range(len(MO)):
		for c in range(len(MO[r])):
			MO[r][c].value = oldMO[r][c].value
	return MO
def recursivelySolve(M):
	if(verifyTable(M)):
		return M
	#trick 1
	m = deepcopy(M)
	m = makeSimpleChanges(m)
	if(verifyTable(m)):
		print("Trick 1 successfull")
		return m
	else:
		#print("Trick 1 failed, trying trick two:")
		pass

	#trick 2
	mo = createMatrixObject(m)
	mo = candidates(mo)
	m = convertMOtoM(mo)
	if(verifyTable(m)):
		print("Trick 2 successfull")
		return m
	else:
		#print("Trick 2 failed, trying trick three:")
		pass

	#trick 3
	if(not verifyTable(m)):
		mo = createMatrixObject(m)
		oldmo = deepcopy(mo)
		coords = coordinatesOfCellWithSmallestValueSet(mo) #This starts getting stuck in an infinite loop between [8, 4] and [8, 5]
		if(coords):
			r = coords[0]
			c = coords[1]
			for guess in mo[r][c].value:
				print("Making guess at: ", coords)
				print("Made guess: ", guess)
				mo[r][c].value = {guess,}
				tempM = convertMOtoM(mo)
				tempM = recursivelySolve(tempM)
				if(verifyTable(tempM)):
					print("Guess successful!")
					return tempM
				else:
					mo = revert(mo, oldmo)
					print("Nope! Reverting and possibly trying again")
	return m

print(verifyTable(M))
printMatrix(M)
print("------Working-----")
M = recursivelySolve(M)
print("-----------------")
print(verifyTable(M))
printMatrix(M)