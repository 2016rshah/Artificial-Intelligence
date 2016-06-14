from random import shuffle, randint, choice
import sys
from collections import Counter
from math import sqrt
import matplotlib.pyplot as plt

#Board represented as:
# [L x y,1,2,3]
# Would be a 4x4 board with queens going down the diagonal

#Internal class for representing locations
class Location:
	def __init__(self, num, st):
		''' num :: Int -- the name/location number of the city
			st :: String -- "42973.333300 12645.000000\n"
		'''
		st = st.strip()
		ns = st.split(" ")
		self.lat = float(ns[0])
		self.lon = float(ns[1])
		self.name = num + 1
	def distanceTo(self, otherLocation):
		'''otherLocation :: Location'''
		x = otherLocation.lat - self.lat
		y = otherLocation.lon - self.lon
		#cache this eventually
		return sqrt(x * x + y * y)
	def latlon(self):
		return (self.lat, self.lon)
	def __str__(self):
		return str(self.name)
	def __repr__(self):
		return str(self)
	def __eq__(self, other):
		# return self.lat == other.lat and self.lon == other.lon
		return self.name == other.name
	def __ne__(self, other):
		return not self.__eq__(other)
	def __hash__(self):
		return hash(self.name)

#Given list of locations, return distance to travel through them
def distanceTraveled(locations):
	''' takes a list of locations
		returns the total distance it would take to travel the entire path '''
	d = 0
	x = len(locations)
	for i in range(0, x - 1):
		d += locations[i].distanceTo(locations[i+1])
	d += locations[x - 1].distanceTo(locations[0])
	return d 

def untangle(fs):
	currDistance = distanceTraveled(fs)
	currPath = list(fs)
	shouldLoop = True
	while shouldLoop:
		shouldLoop = False
		for i in range(0, len(currPath)-2):
			for j in range(i+2, len(currPath)):
				a = i
				b = i+1
				c = j
				if(c+1 < len(currPath)):
					d = j+1
				else:
					d = 0
				incAdd = currPath[a].distanceTo(currPath[c]) + currPath[b].distanceTo(currPath[d])
				incSub = currPath[a].distanceTo(currPath[b]) + currPath[c].distanceTo(currPath[d])
				incDiff = incAdd - incSub
				if(incDiff < 0):
					currPath[b:(c+1)] = reversed(currPath[b:(c+1)])
					currDistance = currDistance + incDiff
					# print("curr distance", currDistance)
					shouldLoop = True
		# plotPath(currPath)
		# plt.pause(0.05)
	return currPath, currDistance

#Input stuff
def getLocations(fn): 
	global N
	f = open(fn, 'r')
	N = int(f.readline())
	fs = [f.readline() for _ in range(N)]
	fs = [Location(i, fs[i]) for i in range(len(fs))]
	return fs

def initialPopulation():
	currParent = getLocations("input_large.txt")
	pop = []
	for _ in range(0, PS):
		shuffle(currParent)
		# print(currParent)
		pop.append((list(currParent), distanceTraveled(currParent)))
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

def findCity(path, predicate):
	for x in range(len(path)):
		if(path[x].name == predicate):
			return path[x]
	print("NOT FOUND")

def mutate(l):
	x = randint(0,10)
	i = randint(0, N-1)
	j = randint(0, N-1)
	#mutations are bad rn
	l[i],l[j] = l[j],l[i]
	return l
	# if(x < 4):
	# 	l[i:j] = reversed(l[i:j])
	# 	return l
	# elif(x < 7):
	# 	l[i], l[j] = l[j], l[i]
	# 	return l
	# else:
		#Need to implement inserting missing city at some point
		# everything = Counter([x for x in range(0, N)])
		# current = Counter([x.name for x in range(len(l))])
		# missing = list(everything - current)
		# extra = list(current - everything)
		# if(len(missing) > 0 and len(extra) > 0):
		# 	# replacementIndex = l.index(Location(extra[0], "-1 -1\n"))
		# 	# replacementIndex = l[extra(0)]
		# 	replacementName = extra[0]
		# 	replacementLocation = findCity(extra[0])
		# 	fakeLocation = Location(replacementName, "-1 -1\n")
		# 	replacementIndex = l.index(fakeLocation)
		# 	l[replacementIndex] = choice(missing)
		# return l

def generateChildren(parent1, parent2):
	p1 = parent1[0] #the list
	p2 = parent2[0]
	pivot = generatePivot()

	p11, p12 = p1[0:pivot], p1[pivot:len(p1)]
	p21, p22 = p2[0:pivot], p2[pivot:len(p1)]

	c1 = p11 + p22
	c2 = p21 + p12
	# c1 = (c1, distanceTraveled(c1))
	c1 = untangle(c1)
	print(c1[1])
	# c2 = (c2, distanceTraveled(c2))
	c2 = untangle(c2)

	#Mutations
	while c1 in P:
		mutated = mutate(c1[0])
		c1 = untangle(mutated)
	while c2 in P:
		mutated = mutate(c2[0])
		# c2 = (mutated, distanceTraveled(mutated))
		c2 = untangle(mutated)
	if (randint(1,10) < 3):
		# print("Mutating both children")
		mutated = mutate(c1[0])
		c1 = untangle(mutated)
		# c1 = (mutated, distanceTraveled(mutated))
		mutated = mutate(c2[0])
		c2 = untangle(mutated)
		# c2 = (mutated, distanceTraveled(mutated))

	
	P.append(c1)
	P.append(c2)
	# print(c1)
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

def plotPath(ls):
	#points
	plt.clf()

	plt.gca().invert_yaxis()
	plt.gca().invert_xaxis()
	xs = map((lambda x: x.lat), ls)
	ys = map((lambda x: x.lon), ls)
	# print(ys)
	plt.scatter(xs, ys, s=5)

	#path
	for i in range(0, len(ls)-1):
		point = ls[i]
		point2 = ls[i+1]
		plt.plot([point.lat, point2.lat], [point.lon, point2.lon])
	point = ls[0]
	point2 = ls[len(ls)-1]
	plt.plot([point.lat, point2.lat], [point.lon, point2.lon])

def main():
	global N 
	global P
	global PS #population size
	plt.ion()
	# N = int(sys.argv[1])
	PS = int(sys.argv[1])
	P = initialPopulation()
	# print(untangle(P[0][0]))
	solution = False
	generation = 0
	while not solution:
		f = P[0][1]
		print("Running generation: ", generation, "with best fitness of", f)
		
		if(P[0][1] < 1570000):
			print(P[0][0])
			plotPath(P[0][0])
			plt.pause(0.05)
			plt.savefig("curr_best.png")

		shuffle(P)
		solution = runGeneration()
		if(solution): break
		P.sort(key=lambda tup: tup[1]) 
		P = P[0:PS]

		generation += 1
	print("Solution for ", N, " with population size ", PS)
	print("Took ", generation, " generations to find")
	print("The solution is", solution)
	while True:
		plt.pause(0.05)
	# print(map(distanceTraveled, P))

if __name__ == "__main__":
	main()