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

def main():
	global N 
	global P
	N = int(sys.argv[1])
	# N = int(raw_input("N: "))
	P = initialPopulation()
	# print(P)
	solution = ([], 0)
	for i in range(0, len(P) - 2, 2):
		j = i + 1
		if(P[i][1] == 0):
			print("Found solution in original population")
			solution = P[i]
			break
		elif(P[j][1] == 0):
			print("Found solution in original population")
			solution = P[j]
			break
		else:
			c1, c2 = generateChildren(P[i], P[j])
			if(c1[1] == 0 ):
				print("Found solution in child")
				solution = c1
				break
			elif(c2[1] == 0):
				print("Found solution in child")
				solution = c2
				break
	print(solution)

	# print(map(numCollisions, P))

if __name__ == "__main__":
	main()