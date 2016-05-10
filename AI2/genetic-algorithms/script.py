from random import shuffle, randint, choice
import sys
from collections import Counter

#Board represented as:
# [0,1,2,3]
# Would be a 4x4 board with queens going down the diagonal

def numCollisions(board):
	cs = 0
	for i in range(0, len(board)-1):
		for j in range(i+1, len(board)):
			iv = board[i]
			ij = board[j]
			#diagonal
			if(abs(iv - ij) == j - i):
				cs+=1
			#rows
			if(board[i] == board[j]):
				cs+=1
	return cs


def initialPopulation():
	currParent = [n for n in range(0, N)]
	pop = []
	for _ in range(0, PS):
		shuffle(currParent)
		# print(currParent)
		pop.append((list(currParent), numCollisions(currParent)))
	# print(pop)
	return pop

def generatePivot():
	x = randint(0,10)
	if(x < 5):
		return N/2 
	elif(x < 7):
		return (N/2) + (N/4)
	elif(x < 9):
		return (N/2) - (N/4)
	else:
		return randint(0, N-1)

def mutate(l):
	x = randint(0,10)
	i = randint(0, N-1)
	j = randint(0, N-1)
	if(x < 4):
		l[i:j] = reversed(l[i:j])
		return l
	elif(x < 7):
		l[i], l[j] = l[j], l[i]
		return l
	else:
		everything = Counter([x for x in range(0, N)])
		current = Counter(l)
		missing = list(everything - current)
		extra = list(current - everything)
		if(len(missing) > 0 and len(extra) > 0):
			replacementIndex = l.index(extra[0])
			l[replacementIndex] = choice(missing)
		# else:
			# l = l[::-1]
		return l

def generateChildren(parent1, parent2):
	p1 = parent1[0] #the list
	p2 = parent2[0]
	pivot = generatePivot()

	p11, p12 = p1[0:pivot], p1[pivot:len(p1)]
	p21, p22 = p2[0:pivot], p2[pivot:len(p1)]

	c1 = p11 + p22
	c2 = p21 + p12
	c1 = (c1, numCollisions(c1))
	c2 = (c2, numCollisions(c2))

	#Mutations
	while c1 in P:
		mutated = mutate(c1[0])
		c1 = (mutated, numCollisions(mutated))
	while c2 in P:
		mutated = mutate(c2[0])
		c2 = (mutated, numCollisions(mutated))
	if (randint(1,10) < 3):
		# print("Mutating both children")
		mutated = mutate(c1[0])
		c1 = (mutated, numCollisions(mutated))
		mutated = mutate(c2[0])
		c2 = (mutated, numCollisions(mutated))

	
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
	global PS #population size
	N = int(sys.argv[1])
	PS = int(sys.argv[2])
	# N = int(raw_input("N: "))
	P = initialPopulation()
	# print(P)
	solution = False
	# for generation in range(0, 200):
	generation = 0
	while not solution:
		f = P[0][1]
		print("Running generation: ", generation, "with best fitness of", f)
		if(f < 2):
			print(P[0])
		shuffle(P)
		solution = runGeneration()
		if(solution): break
		P.sort(key=lambda tup: tup[1]) 
		P = P[0:PS]

		generation += 1
	print("Solution for ", N, " with population size ", PS)
	print("Took ", generation, " generations to find")
	print("The solution is", solution)

	# print(map(numCollisions, P))

if __name__ == "__main__":
	main()