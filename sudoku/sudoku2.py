"""
+---------------+
|Rushi Shah		|
|11/19/14		|
|AI 6th period	|
+---------------+
"""
from copy import deepcopy
from time import sleep
ROWS = 9
COLS = 9
count = 0
guessesMade = {}

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
def badMatrix(MO):
	for r in range(len(MO)):
		for c in range(len(MO[r])):
			if(MO[r][c].value == set()):
				return True 
	return False
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
def makeSimpleChanges(m):
	#m = deepcopy(M)
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
	if(mo == None):
		exit()
	return mo
def createMatrixObject(M):
	matrix = []
	for r in range(9):
		row = []
		for c in range(9):
			row.append(Cell(M[r][c], r, c, matrix))
		matrix.append(row)
	matrix = candidates(matrix)
	return matrix
def printMatrixObject(MO):
	print("\n")
	for row in range(len(MO)):
		s = ""
		for col in range(len(MO[row])):
			if(len(MO[row][col].value)==1):
				s+=str((MO[row][col].value))
			else:

				s+="{0}"
		print(s)
	print("\n")
def convertMOtoM(mo):
	res = []
	for i in range(len(mo)):
		res.append([])
		for j in range(len(mo[i])):
			res[i].append(0)
			if(len(mo[i][j].value) == 1):
				res[i][j] = mo[i][j].value.pop()
	return res
# def coordinatesOfCellWithSmallestValueSet(MO):
# 	big = float('inf')
# 	sml = 2
# 	bestRow = -1
# 	bestCol = -1
# 	for r in range(len(MO)):
# 		for c in range(len(MO[r])):
# 			length = len(MO[r][c].value)
# 			if sml<=length < big:
# 				big = length
# 				bestRow = r
# 				bestCol = c
# 	if bestRow == -1 or bestCol == -1:
# 		printMatrixObject(MO)
# 		exit("Error in coords")
# 	return (bestRow, bestCol)

def orderedCoords(mo):
	#mo = deepcopy(MO)
	mo = candidates(mo)
	#print(mo)
	coords = []
	for i in range(len(mo)):
		for j in range(len(mo[i])):
			if(len(mo[i][j].value)>1):
				coords.append([len(mo[i][j].value), i, j])
	coords.sort(key = lambda x: x[0])
	while(True):
		if(len(coords)>0 and len(mo[coords[0][1]][coords[0][2]].value)>1):
			#print("Guess location: ", coords[0][1], coords[0][2])
			#print("Guess options: ", mo[coords[0][1]][coords[0][2]].value)
			#m = convertMOtoM(mo)
			#sleep(.5)
			#print("\n"*50)
			#printMatrix(m)
			return coords
		else:
			#print("-"*50, coords)
			return []
def revert(MO, oldMO):
	# for r in range(len(MO)):
	# 	for c in range(len(MO[r])):
	# 		MO[r][c].value = oldMO[r][c].value
	# m = convertMOtoM(MO)
	# printMatrix(m)
	# return MO
	MO = deepcopy(oldMO)
	#printMatrixObject(MO)
	return MO
def badMatrix(matrix):
	for r in range(len(matrix)):
		for c in range(len(matrix[r])):
			if(matrix[r][c].value == set()):
				return True
	return False
def trick12(M):
	m = deepcopy(M)
	if(verifyTable(m)):
		return m
	#trick 1
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
		#printMatrix(m)
	return m
def recursivelySolve(m):
	mo = createMatrixObject(m)
	if(badMatrix(mo)):
		return m
	global count
	count+=1
	#print("count: ", count)
	m = trick12(m)
	#trick 3
	mo = createMatrixObject(m)
	oldmo = deepcopy(mo)
	coords = orderedCoords(mo)
	if(len(coords) > 1):
		for coord in coords:
			r = coord[1]
			c = coord[2]
			mo = candidates(mo)
			for guess in mo[r][c].value:
				if((r, c)in guessesMade):
					if(guess in guessesMade[(r, c)]):
						continue
					guessesMade[(r, c)].append(guess)
				else:
					guessesMade[(r, c)] = [guess]
				print("-"*count, [r, c], mo[r][c].value)
				mo[r][c].value = {guess,}
				tempM = convertMOtoM(mo)
				#printMatrix(m)
				tempM = recursivelySolve(tempM)
				count-=1
				#print("count: ", count)
				if(verifyTable(tempM)):
					print("Guess successful!")
					return tempM
				else:
					#print("Guess unsuccessful, reverting")
					#printMatrixObject(oldmo)
					mo = revert(mo, oldmo)
					#printMatrixObject(mo)
					#print("Nope! Reverting and possibly trying again")
					#perhaps here I need to take the guess I made out of being a candidate...
	else:
		mo = revert(mo, oldmo)
	return m
# def recursivelySolveTheSudoku(m):
# 	m = trick12(m)
# 	if(verifyTable(m)):
# 		exit()
# 	mo = createMatrixObject(m) 
# 	oldmo = deepcopy(mo)
# 	r,c = coordinatesOfCellWithSmallestValueSet(mo)
# 	for guess in mo[r][c].value:
# 		mo[r][c].value = {guess,}
# 		m = convertMOtoM(mo)
# 		m = recursivelySolveTheSudoku(m)
# 		# mo  = createMatrixObject(m)
# 		if(verifyTable(m)):
# 			return m
# 		mo = revert(mo, oldmo)
# 	return m
 
def main():
	M = [
		[0,3,2,0,0,0,0,0,0],
		[6,8,0,9,0,0,0,0,5],
		[0,1,0,0,0,4,0,7,0],
		[1,0,0,0,0,9,7,3,0],
		[0,7,9,6,0,3,4,8,0],
		[0,4,6,7,0,0,0,0,1],
		[0,9,0,5,0,0,0,2,0],
		[8,0,0,0,0,1,0,9,7],
		[0,0,0,0,0,0,6,1,0]
	] #works	
	print(verifyTable(M))
	printMatrix(M)
	print("------Working-----")
	M = recursivelySolve(M)
	print("-----------------")
	print(verifyTable(M))
	printMatrix(M)
main()
#I think it is infinite recursion because I let it run for like a minute...