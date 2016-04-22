from math import sqrt
import matplotlib.pyplot as plt


THRESHOLD_ONE = 10000
THRESHOLD_TWO = 100

# CACHE = set()

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
		x1 = self.lat
		y1 = self.lon
		x2 = otherLocation.lat
		y2 = otherLocation.lon
		x = x2 - x1
		y = y2 - y1
		return sqrt(x * x + y * y)
	def __str__(self):
		return str(self.name)
	def __repr__(self):
		return str(self)

#Input stuff
def getLocations(): 
	f = open("input_medium.txt", 'r')
	x = int(f.readline())
	fs = [f.readline() for _ in range(x)]
	fs = [Location(i, fs[i]) for i in range(len(fs))]
	return fs

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

def allPossibleSwaps(s):
	ss = []
	for i in range(0, len(s)):
		for j in range(0, len(s)):
			# if(i is not j):
				s[i], s[j] = s[j], s[i]
				# if(str(s) not in CACHE):
				# 	CACHE.add(str(s))
				yield s #generator that won't store everything in memory
				# else:
				# 	print("cache helped")
	# return ss

#Cycle through list until you're starting at location 1
def startFrom1(fs):
	''' given a list of locations
		return a list of locations
		post-condition: the list will start with the location #1
		'''
	while (fs[0].name is not 1):
		fs.append(fs.pop(0))
	return fs

#output stuff
def plotPath(ls):
	#points
	plt.clf()
	xs = map((lambda x: x.lat), ls)
	ys = map((lambda x: x.lon), ls)
	plt.scatter(xs, ys)

	#path
	for i in range(0, len(ls)-1):
		point = ls[i]
		point2 = ls[i+1]
		plt.plot([point.lat, point2.lat], [point.lon, point2.lon])
	point = ls[0]
	point2 = ls[len(ls)-1]
	plt.plot([point.lat, point2.lat], [point.lon, point2.lon])

#actual AI stuff
def findBestSwap(fs):
	#this is the best for one swap, but then you feed this best swap back in to get an even better guess
	originalMin = distanceTraveled(fs)
	currMin = originalMin
	bestSwap = list(fs)
	swapsSinceImprovement = 0
	for swap in allPossibleSwaps(fs):
		d = distanceTraveled(swap)
		if(d < currMin):
			# print("improved to", d)
			swapsSinceImprovement = 0
			currMin = d
			bestSwap = list(swap)
		else:
			swapsSinceImprovement += 1
		if(swapsSinceImprovement > THRESHOLD_ONE):
			print("haven't improved in a while, breaking")
			break
	#recursive solution:
	# if(originalMin is not currMin):
	# 	print("recursing with new best of: ", currMin)
	# return findBestSwap(bestSwap)
	#iterative solution:
	return bestSwap


plt.ion()
distanceImprovedSinceLastSwap = 0
fs = getLocations()
print(len(fs))
currMin = distanceTraveled(fs)
print(currMin)
currSwap = list(fs)
swapsSinceImprovement = 0
for i in range(0, 10000):
	bestswap = findBestSwap(currSwap)
	d = distanceTraveled(bestswap)
	if(d < currMin):
		print("Found new best distance: ", d)
		if(distanceImprovedSinceLastSwap > 250):
			distanceImprovedSinceLastSwap = 0
			plotPath(currSwap)
			plt.pause(0.05)
		else:
			distanceImprovedSinceLastSwap += (currMin - d)
			print("not a great improvement", distanceImprovedSinceLastSwap)
		currSwap = list(bestswap)
		currMin = d
		swapsSinceImprovement = 0
	else:
		swapsSinceImprovement += 1
	if(swapsSinceImprovement > THRESHOLD_TWO):
		print("Haven't improved in about ", swapsSinceImprovement, " swaps, so exiting at")
		break

bestPath = startFrom1(currSwap)
print(bestPath)
print(distanceTraveled(bestPath))
plotPath(bestPath)

while True:
    plt.pause(0.05)


