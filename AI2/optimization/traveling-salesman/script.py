from math import sqrt
import matplotlib.pyplot as plt
from random import shuffle


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
		return self.lat == other.lat and self.lon == other.lon
	def __ne__(self, other):
		return not self.__eq__(other)

#Input stuff
def getLocations(fn): 
	f = open(fn, 'r')
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

def fancyDistanceTraveled(ordered, locations):
	# ordered = [L 1 x y, L 2 x y]
	# locations = [1,2,3,4]
	x = len(locations)

	d = 0
	for j in range(0, x-1):
		x = locations[j]-1
		y = locations[j+1]-1
		d += ordered[x].distanceTo(ordered[y])
	d += ordered[x - 1].distanceTo(ordered[0])
	return d 

def calc():
	fs = getLocations("input_large.txt")
	# x = [384, 167, 706, 222, 32, 504, 719, 639, 691, 527, 699, 658, 612, 439, 422, 80, 33, 162, 243, 513, 116, 256, 665, 122, 113, 308, 597, 582, 264, 592, 200, 226, 191, 292, 287, 397, 675, 360, 164, 460, 655, 411, 731, 180, 668, 538, 408, 319, 428, 203, 703, 274, 320, 293, 260, 251, 266, 369, 362, 351, 492, 286, 8, 302, 594, 127, 413, 268, 424, 171, 195, 389, 466, 347, 552, 25, 536, 479, 452, 310, 399, 634, 272, 406, 348, 710, 436, 24, 110, 700, 433, 475, 313, 633, 81, 696, 718, 31, 239, 562, 390, 677, 78, 520, 500, 581, 285, 65, 172, 215, 336, 128, 342, 508, 618, 621, 358, 175, 28, 725, 648, 54, 45, 531, 252, 400, 484, 29, 404, 199, 578, 733, 546, 469, 423, 503, 584, 528, 637, 418, 554, 350, 441, 474, 610, 246, 535, 41, 666, 728, 92, 51, 443, 726, 470, 255, 414, 695, 446, 103, 688, 600, 108, 669, 43, 85, 704, 684, 517, 19, 523, 613, 442, 132, 543, 134, 343, 227, 625, 478, 223, 26, 64, 325, 494, 289, 567, 316, 732, 218, 602, 105, 383, 515, 682, 412, 697, 37, 74, 204, 290, 483, 312, 18, 727, 23, 714, 624, 68, 642, 606, 444, 519, 123, 674, 656, 153, 388, 647, 393, 361, 208, 573, 303, 453, 717, 209, 572, 98, 345, 96, 70, 505, 62, 589, 329, 154, 420, 170, 603, 158, 435, 544, 133, 676, 518, 254, 163, 447, 617, 681, 137, 193, 643, 605, 364, 3, 627, 247, 104, 58, 486, 729, 394, 66, 545, 334, 595, 106, 326, 410, 57, 178, 571, 583, 387, 234, 705, 148, 461, 521, 121, 568, 307, 185, 405, 224, 190, 83, 118, 48, 338, 662, 407, 491, 131, 124, 593, 522, 273, 323, 381, 651, 321, 21, 694, 76, 590, 395, 306, 493, 534, 337, 480, 547, 630, 354, 709, 109, 487, 477, 377, 240, 101, 194, 213, 73, 5, 511, 353, 179, 249, 623, 646, 501, 403, 524, 507, 352, 425, 664, 1, 67, 599, 277, 672, 680, 220, 438, 56, 401, 267, 376, 202, 284, 720, 661, 569, 451, 650, 295, 71, 94, 601, 10, 711, 6, 235, 143, 620, 112, 472, 457, 59, 147, 587, 730, 35, 138, 248, 532, 667, 375, 159, 9, 188, 576, 86, 485, 499, 359, 135, 301, 214, 297, 327, 257, 219, 315, 712, 15, 653, 607, 333, 378, 245, 541, 628, 721, 97, 40, 716, 432, 657, 416, 366, 46, 111, 300, 211, 217, 100, 229, 398, 335, 660, 596, 454, 386, 371, 262, 430, 242, 176, 38, 462, 299, 679, 468, 448, 591, 431, 632, 402, 250, 367, 641, 580, 526, 253, 72, 139, 509, 449, 370, 471, 141, 631, 99, 155, 465, 82, 91, 198, 331, 611, 380, 14, 683, 498, 181, 4, 125, 690, 282, 317, 182, 231, 136, 129, 225, 459, 52, 2, 340, 450, 678, 671, 241, 540, 564, 216, 309, 75, 619, 722, 174, 305, 53, 237, 529, 324, 356, 693, 298, 502, 357, 427, 649, 288, 372, 652, 608, 445, 698, 488, 189, 355, 560, 238, 506, 236, 60, 107, 409, 270, 114, 281, 173, 271, 495, 278, 598, 294, 152, 559, 102, 187, 577, 654, 206, 629, 30, 707, 183, 476, 201, 553, 686, 548, 318, 280, 626, 276, 701, 379, 87, 169, 604, 344, 429, 205, 90, 385, 723, 84, 258, 146, 575, 702, 95, 579, 496, 382, 455, 55, 614, 392, 69, 332, 464, 549, 609, 157, 724, 537, 61, 467, 685, 17, 166, 550, 93, 481, 79, 311, 322, 144, 117, 119, 556, 516, 232, 673, 265, 551, 426, 197, 50, 373, 16, 11, 525, 514, 88, 396, 150, 186, 330, 616, 539, 497, 588, 561, 165, 328, 473, 279, 269, 156, 555, 42, 140, 349, 263, 36, 574, 296, 177, 463, 77, 151, 563, 339, 490, 622, 44, 115, 374, 415, 12, 210, 212, 421, 228, 638, 692, 291, 365, 283, 126, 207, 530, 615, 437, 670, 120, 89, 689, 440, 130, 565, 636, 341, 34, 230, 27, 659, 47, 314, 63, 512, 586, 368, 482, 458, 161, 221, 708, 39, 570, 233, 456, 149, 489, 160, 645, 734, 346, 168, 244, 22, 566, 715, 142, 196, 417, 261, 145, 533, 542, 363, 585, 49, 640, 259, 713, 663, 510, 434, 391, 304, 20, 558, 687, 635, 557, 419, 13, 644, 7, 192, 275, 184]
	# x = [1..734]
	print(fancyDistanceTraveled(fs, x))

def swap(xs, i, j):
	#out of place swap
	c = list(xs)
	c[i], c[j] = c[j], c[i]
	return c

def allPossibleSwaps(s):
	# ss = []
	for i in range(0, len(s)):
		for j in range(0, len(s)):
			# if(i is not j):
				s[i], s[j] = s[j], s[i]
				# if(str(s) not in CACHE):
				# 	CACHE.add(str(s))
				yield s
				# ss.append(swap(s,i,j))
				# yield cs #generator that won't store everything in memory
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
	if(fs[1].name > fs[len(fs)-1].name):
		fs[1:len(fs)] = reversed(fs[1:len(fs)])
	return fs

#output stuff
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
	return bestSwap

def loopThroughAllPossibilities(fs):
	distanceImprovedSinceLastSwap = 0
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
	return currSwap

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

def combineMethods(fs):
	currMin = distanceTraveled(fs)
	print(currMin)
	currSwap = list(fs)
	swapsSinceImprovement = 0
	# for i in range(0, 10):
	bestswap = findBestSwap(currSwap)
	d = distanceTraveled(bestswap)
	if(d < currMin):
		bestswap, d = untangle(bestswap)
		print("Found new best distance: ", d, distanceTraveled(bestswap))
		currSwap = list(bestswap)
		currMin = d
		swapsSinceImprovement = 0
		plotPath(currSwap)
		plt.pause(0.05)
	else:
		swapsSinceImprovement += 1
		# print("iterating at", currMin)
		# print("iterating")
		# if(swapsSinceImprovement > THRESHOLD_TWO):
		# 	print("Haven't improved in about ", swapsSinceImprovement, " swaps, so exiting at")
		# 	break
	return currSwap

def shuffleAndUntangle(fs):
	currPath = list(fs)
	currDistance = float(open('curr_results.txt', "r").readline().strip())
	print("looking for an improvement on", currDistance)
	#86479.99063636374
	while True:
		shuffle(currPath)
		newPath, newDistance = untangle(currPath)
		# print("newPath", newPath)
		print("newDistance", newDistance)
		if(newDistance < currDistance):
			print("improved by", currDistance - newDistance)
			currPath = startFrom1(newPath)
			currDistance = newDistance

			#output to console
			print(currDistance)
			print(currPath)

			#output picture
			plotPath(currPath)
			plt.pause(0.05)
			plt.savefig("curr_best.pdf")

			#clear previous results in file
			open('curr_results.txt', 'w').close()

			#write results to file
			f = open('curr_results.txt', 'w')
			f.write(str(currDistance))
			f.write("\n")
			f.write(str(currPath))
		plotPath(newPath)
		plt.pause(0.05)

def genImage(path):
	ordered = getLocations("input_large.txt")
	locationPath = []
	for i in path:
		locationPath.append(ordered[i-1])
	plotPath(locationPath)
	plt.pause(0.05)
	plt.savefig("results.png")

def main():
	plt.ion()
	fs = getLocations("input_large.txt")

	print("beginning distance:",distanceTraveled(fs))

	# bestPath = loopThroughAllPossibilities(fs)
	
	# bestPath = combineMethods(fs)

	bestPath = shuffleAndUntangle(fs)
	bestPath = startFrom1(bestPath)
	
	# bestPath = [1, 3, 6, 11, 22, 25, 58, 68, 67, 76, 75, 74, 105, 72, 73, 63, 54, 50, 44, 41, 53, 56, 66, 83, 95, 100, 123, 124, 121, 120, 126, 98, 92, 69, 60, 55, 51, 43, 39, 40, 34, 28, 21, 19, 17, 26, 24, 23, 15, 10, 8, 7, 2, 5, 4, 12, 13, 9, 14, 20, 29, 31, 38, 42, 49, 65, 71, 104, 113, 134, 132, 125, 143, 147, 151, 140, 142, 137, 131, 108, 119, 112, 107, 111, 114, 88, 89, 90, 70, 62, 57, 52, 37, 33, 30, 32, 35, 48, 59, 61, 82, 64, 78, 87, 99, 103, 96, 97, 117, 130, 135, 149, 154, 153, 146, 174, 183, 194, 219, 225, 223, 218, 232, 238, 217, 211, 202, 173, 177, 201, 198, 152, 148, 145, 141, 138, 122, 106, 94, 101, 102, 129, 128, 116, 136, 144, 164, 158, 172, 188, 185, 193, 197, 206, 216, 222, 214, 228, 250, 254, 282, 303, 315, 307, 283, 275, 258, 259, 255, 288, 287, 286, 290, 299, 308, 320, 350, 354, 367, 349, 327, 319, 309, 279, 249, 204, 210, 221, 278, 285, 293, 297, 302, 318, 358, 361, 362, 366, 382, 398, 407, 397, 396, 385, 393, 388, 403, 415, 440, 452, 464, 461, 468, 467, 495, 549, 593, 608, 594, 565, 553, 546, 545, 540, 531, 516, 482, 524, 532, 566, 595, 667, 634, 652, 692, 712, 723, 734, 724, 693, 679, 668, 661, 641, 603, 569, 596, 568, 554, 547, 528, 496, 474, 469, 471, 444, 456, 466, 427, 399, 391, 394, 404, 425, 445, 428, 429, 420, 409, 389, 377, 376, 356, 311, 333, 304, 273, 260, 276, 310, 323, 334, 342, 351, 341, 355, 344, 359, 363, 347, 380, 383, 373, 406, 405, 417, 441, 430, 433, 431, 437, 457, 477, 487, 502, 505, 491, 484, 450, 434, 432, 423, 413, 414, 386, 369, 360, 329, 339, 328, 300, 321, 324, 316, 298, 291, 264, 241, 226, 203, 189, 175, 166, 155, 139, 150, 159, 156, 160, 157, 161, 163, 168, 179, 167, 178, 176, 200, 186, 199, 207, 230, 233, 235, 251, 243, 239, 224, 220, 227, 231, 244, 274, 284, 277, 267, 268, 272, 280, 305, 330, 335, 346, 345, 371, 370, 378, 400, 435, 458, 442, 436, 422, 418, 408, 410, 416, 438, 439, 448, 451, 446, 447, 459, 453, 479, 465, 470, 480, 490, 500, 494, 485, 493, 508, 499, 498, 489, 492, 488, 503, 511, 548, 564, 586, 588, 604, 610, 616, 624, 619, 615, 606, 599, 592, 573, 605, 609, 631, 640, 643, 655, 658, 646, 645, 644, 629, 628, 627, 638, 625, 570, 555, 552, 541, 534, 533, 497, 478, 475, 486, 507, 530, 538, 529, 510, 506, 521, 525, 550, 561, 582, 597, 583, 587, 598, 563, 574, 620, 647, 626, 648, 636, 635, 639, 653, 683, 694, 675, 676, 656, 670, 684, 680, 689, 649, 662, 673, 677, 657, 669, 681, 686, 699, 711, 716, 722, 706, 707, 702, 703, 700, 698, 690, 682, 674, 660, 654, 651, 666, 672, 678, 685, 688, 695, 696, 705, 709, 708, 704, 701, 710, 713, 718, 717, 714, 725, 726, 727, 732, 733, 729, 728, 730, 731, 719, 720, 721, 715, 697, 691, 687, 663, 659, 650, 664, 671, 665, 642, 637, 607, 577, 581, 562, 571, 578, 600, 601, 557, 560, 556, 542, 514, 535, 537, 567, 590, 580, 575, 579, 584, 611, 617, 589, 612, 621, 602, 630, 613, 618, 622, 632, 633, 623, 614, 591, 576, 585, 572, 523, 504, 517, 512, 476, 462, 454, 419, 387, 384, 374, 375, 412, 426, 443, 460, 455, 472, 483, 513, 519, 509, 518, 527, 539, 526, 536, 558, 559, 551, 543, 544, 522, 520, 515, 501, 481, 473, 463, 449, 421, 379, 402, 357, 326, 325, 322, 313, 337, 338, 348, 353, 372, 401, 381, 395, 424, 411, 390, 392, 368, 364, 340, 336, 332, 301, 252, 236, 234, 205, 208, 261, 265, 266, 294, 306, 312, 343, 365, 352, 331, 317, 296, 295, 269, 292, 245, 253, 237, 212, 262, 270, 263, 289, 281, 246, 256, 247, 257, 314, 271, 248, 242, 240, 229, 209, 213, 182, 181, 192, 215, 196, 187, 184, 171, 170, 169, 195, 191, 190, 180, 165, 162, 109, 110, 118, 133, 127, 115, 91, 86, 81, 80, 79, 85, 84, 93, 77, 46, 45, 36, 47, 27, 18, 16]
	# genImage(bestPath)

	print(bestPath)
	print(distanceTraveled(bestPath))
	plotPath(bestPath)
	while True:
		plt.pause(0.05)

if __name__ == "__main__":
	main()
