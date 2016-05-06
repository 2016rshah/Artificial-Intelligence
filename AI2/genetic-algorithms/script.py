from random import shuffle
import sys

#Board represented as:
# [0,1,2,3]
# Would be a 4x4 board with queens going down the diagonal

def numCollisions(board):
	cs = 0
	n = len(board)
	for i in range(0, n):
		j = board[i] 
		di = i 
		dj = j 
		while(di < n and dj < n and di < n and dj < n):
			if(board[di] == dj):
				cs += 1
				# print(di, dj)
			di += 1
			dj += 1
		cs -= 1

		di = i
		dj = j
		while(di >= 0 and dj >= 0 and di < n and dj < n):
			if(board[di] ==  dj):
				cs += 1
				# print(di, dj)
			di -= 1
			dj -= 1
		cs -= 1

		di = i 
		dj = j
		while(di >= 0 and dj >= 0 and di < n and dj < n):
			if(board[di] == dj):
				cs += 1
				# print(di, dj)
			di += 1
			dj -= 1
		cs -= 1

		di = i
		dj = j 
		while(di >= 0 and dj >= 0 and di< n and dj < n):
			if(board[di] == dj):
				cs += 1
				# print(di, dj)
			di -= 1
			dj += 1
		cs -= 1
	return cs

def initialPopulation():
	currParent = [n for n in range(0, N)]
	pop = []
	for _ in range(0, 100):
		shuffle(currParent)
		# print(currParent)
		pop.append((list(currParent), numCollisions(currParent)))
	# print(pop)
	return pop

def generatePivot():
	return N/2 

def mutate(l):
	#As of right now just mutate by reversing
	return l[::-1]

def generateChildren(parent1, parent2):
	p1 = parent1[0] #the list
	p2 = parent2[0]
	pivot = generatePivot()

	p11, p12 = p1[0:pivot], p1[pivot:len(p1)]
	p21, p22 = p2[0:pivot], p2[pivot:len(p1)]
	assert(len(p21) + len(p22) == len(p2))

	c1 = p11 + p22
	c2 = p21 + p12

	if c1 in P:
		c1 = mutate(c1)
	if c2 in P:
		P.append(c2)

	c1 = (c1, numCollisions(c1))
	c2 = (c2, numCollisions(c2))
	P.append(c1)
	P.append(c2)
	return (c1, c2)

def runGeneration():
	for i in range(0, len(P) - 2, 2):
		j = i + 1
		if(i < N):
			if(P[i][1] == 0):
				print("Found solution in original population")
				solution = P[i]
				return solution
			elif(P[j][1] == 0):
				print("Found solution in original population")
				solution = P[j]
				return solution
		else:
			c1, c2 = generateChildren(P[i], P[j])
			if(c1[1] == 0 ):
				print("Found solution in child")
				solution = c1
				return solution
			elif(c2[1] == 0):
				print("Found solution in child")
				solution = c2
				return solution
	return False

def main():
	global N 
	global P
	N = int(sys.argv[1])
	# N = int(raw_input("N: "))
	P = initialPopulation()
	# print(P)
	solution = False
	while not solution:
		print("Running generation with population of", len(P))
		solution = runGeneration()
		P.sort(key=lambda tup: tup[1]) 
	print(solution)

	
	print(solution)

	# print(map(numCollisions, P))

if __name__ == "__main__":
	main()