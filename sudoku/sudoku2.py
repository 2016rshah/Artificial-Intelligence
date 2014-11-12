ROWS = 9
COLS = 9
M = [
    [4, 8, 1, 5, 0, 9, 6, 7, 0],
    [3, 0, 0, 8, 1, 6, 0, 0, 2],
    [5, 0, 0, 7, 0, 3, 0, 0, 8],
    [2, 0, 0, 0, 0, 0, 0, 0, 9],
    [9, 0, 0, 0, 0, 0, 0, 0, 1],
    [8, 0, 0, 0, 0, 0, 0, 0, 4],
    [0, 3, 9, 2, 7, 5, 4, 8, 0],
    [6, 0, 0, 0, 0, 0, 9, 2, 7],
    [7, 0, 0, 0, 0, 0, 3, 1, 0]
]

SOLVED = [
	[4,8,3,9,2,1,6,5,7],
	[9,6,7,3,4,5,8,2,1],
	[2,5,1,8,7,6,4,9,3],
	[5,4,8,1,3,2,9,7,6],
	[7,2,9,5,6,4,1,3,8],
	[1,3,6,7,9,8,2,4,5],
	[3,7,2,6,8,9,5,1,4],
	[8,1,4,2,5,3,7,6,9],
	[6,9,5,4,1,7,3,8,2]
]

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
			elif(m[i][j] == 0):

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

print(verifyTable(M))
print(verifyTable(SOLVED))