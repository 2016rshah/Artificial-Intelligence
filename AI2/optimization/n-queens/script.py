# N-Queens problem
# Input as an array of n numbers less than n that each represent the column the queen is in

from random import shuffle
from math import factorial

import numpy as np
import matplotlib.pyplot as plt

#Board represented as:
# [0,1,2,3]
# Would be a 4x4 board with queens going down the diagonal

def numCollisions(board):
	cs = 0
	n = len(board)
	for i in range(0, n):
		for j in range(0, n):
			if(board[i] == j):
				#check 
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

def nchoose2(n):
	return factorial(n) / factorial(n-2)

def minShuffleCollisions(board):
	currMin = numCollisions(board)
	bounds = int(nchoose2(len(s)))
	for i in range(0, bounds):
		shuffle(board)
		cs = numCollisions(board)
		if(cs < currMin):
			#print("found a new min", s)
			currMin = cs
	return currMin

def swap(l, i, j):
	l[i], l[j] = l[j], l[i]
	return l

def allPossibleSwaps(s):
	swaps = []
	for i in range(0, len(s)):
		for j in range(0, len(s)):
			if(i is not j):
				swaps.append(swap(s, i, j))
	return swaps

def findGoodSwap(board):
	currMin = numCollisions(board)
	ops = 0
	for swap in allPossibleSwaps(board):
		board = swap
		cs = numCollisions(board)
		if(cs == currMin):
			ops += 1
			# print("found a lateral swap")
		elif(cs < currMin):
			# print("found a good swap")
			return (swap, ops)
	# print("couldn't find a good swap")
	return (-1, ops)

def partA(board):
	currMin = numCollisions(board)
	numShuffles = 0
	numSwaps = 0
	numOpportunities = 0
	while currMin is not 0:
		r, lateral = findGoodSwap(board)
		if(r == -1):
			shuffle(board)
			numShuffles += 1
			# print("had to shuffle")
		else:
			s = r 
			numSwaps += 1
			numOpportunities += lateral
		currMin = numCollisions(board)
	return (numSwaps, numShuffles, lateral)

def plotPartA():
	plt.figure(1)
	lb = 4
	ub = 10
	numTrials = 5
	ns = [x for x in range(lb, ub)]
	# ws = [] #swaps
	wss = [[] for _ in range(lb,ub)]
	# fs = [] #shuffles
	fss = [[] for _ in range(lb,ub)]
	oss = [[] for _ in range(lb, ub)]
	for _ in range(0,numTrials): #repeated trials
		for n in range(lb, ub):
			s = [x+1 for x in range(0, n)]
			numSwaps, numShuffles, numOpportunities = partA(s)
			wss[n-lb].append(numSwaps)
			fss[n-lb].append(numShuffles)
			oss[n-lb].append(numOpportunities)
		print("finished a trial")
	ws = map(np.median, wss)
	fs = map(np.median, fss)
	os = map(np.max, oss)
	print(wss)
	print(fss)
	print(ws)
	print(fs)
	plt.xlabel("N")
	plt.ylabel("Number of swaps/shuffles")
	plt.plot(ns, ws, linewidth=2, label="Swaps")
	plt.plot(ns, fs, linewidth=2, label="Shuffles")
	plt.plot(ns, os, linewidth=2, label="Laterals")
	plt.legend()
	plt.xticks(ns)
	plt.title("Part A")


def findOkaySwap(board):
	currMin = numCollisions(board)
	for swap in allPossibleSwaps(board):
		board = swap
		cs = numCollisions(board)
		if(cs < currMin):
			# print("found a good swap")
			return swap
		elif(cs == currMin):
			# print("found an okay swap")
			return swap
	# print("couldn't find a okay swap")
	return -1
	
def partB(board):
	currMin = numCollisions(board)
	numShuffles = 0
	numSwaps = 0
	while currMin is not 0:
		r = findOkaySwap(board)
		if(r == -1):
			shuffle(board)
			numShuffles += 1
			# print("had to shuffle")
		else:
			s = r 
			numSwaps += 1
			# print("swapping")
		currMin = numCollisions(board)
	return (numSwaps, numShuffles)

def plotPartB():
	plt.figure(2)
	lb = 5
	ub = 9
	numTrials = 1
	ns = [x for x in range(lb, ub)]
	# ws = [] #swaps
	wss = [[] for _ in range(lb,ub)]
	# fs = [] #shuffles
	fss = [[] for _ in range(lb,ub)]
	for _ in range(0,numTrials): #repeated trials
		for n in range(lb, ub):
			s = [x+1 for x in range(0, n)]
			numSwaps, numShuffles= partB(s)
			wss[n-lb].append(numSwaps)
			fss[n-lb].append(numShuffles)
		print("finished a trial")
	ws = map(np.median, wss)
	fs = map(np.median, fss)
	print(wss)
	print(fss)
	print(ws)
	print(fs)
	plt.xlabel("N")
	plt.ylabel("Number of swaps/shuffles")
	plt.plot(ns, ws, linewidth=2, label="Swaps")
	plt.plot(ns, fs, linewidth=2, label="Shuffles")
	
	plt.legend()
	plt.xticks(ns)
	plt.title("Part B")

# plotPartA()
plotPartB()
plt.show()