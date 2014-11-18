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
	[0,8,0,9,2,1,6,5,7],
	[9,0,0,3,4,5,8,2,1],
	[2,5,1,8,7,6,4,9,3],
	[5,4,8,1,3,2,9,7,6],
	[7,2,9,5,6,4,1,3,8],
	[1,3,6,7,9,8,2,4,5],
	[3,7,2,6,8,9,5,1,4],
	[8,1,4,2,5,3,7,6,9],
	[6,9,5,4,1,7,3,8,2]
]


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
def fillRows(m):
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
			print("replaced..")
	return m
def fillCols(m):
	#check rows
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
			print("replaced..")
	return m
def fillBoxes(m):
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
				print("replaced..")
	return m
def iterativelySolve(m):
	count = 0
	while(not verifyTable(m)):
		m = fillRows(m)
		m = fillCols(m)
		m = fillBoxes(m)
		count+=1
		if(count>5000):
			print("it took a while, gave up")
			exit()
	print("Success! Iterations: ", count)
	return m
printMatrix(M)
print("------Working-----")
M = iterativelySolve(M)
print("-----------------")
printMatrix(M)