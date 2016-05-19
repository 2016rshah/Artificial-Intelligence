#Expected to use Python 3!!

from math import e

def f(w, b, x):
	return 1 / (1 + (e ** (-w * x + b)))

def g(w,b,x,y):
	return 1 / (1 + (e ** (-w * (x+y) + b)))

# not -> singleValueHillClimbing([0,1],[1,0])
def singleValueHillClimbing(xs, ys):
	bestW = 0
	bestB = 0
	bestError = 100000000
	w = 100
	b = 100
	while w > -100:
		while b > -100:
			# print(w,b)
			currError = 0
			for i in range(len(xs)):
				currError += (ys[i] - f(w, b, xs[i])) ** 2
			# print(w,b,currError)
			if(currError < bestError):
				bestError = currError
				bestW = w
				bestB = b
				print(bestW, bestB, currError)
			b -= .1
		b = 100
		w -= .1

# # AND
# # 0 -> 0 -> 0
# # 0 -> 1 -> 0
# # 1 -> 0 -> 0
# # 1 -> 1 -> 1
# [0,0,1,1]
# [0,1,0,1]
# [0,0,0,1]

# # OR
# # 0 -> 0 -> 0
# # 0 -> 1 -> 1
# # 1 -> 0 -> 1
# # 1 -> 1 -> 1
# [0,0,1,1]
# [0,1,0,1]
# [0,1,1,1]

# doubleValueHillClimbing([0,1],[1,0])
def doubleValueHillClimbing(xs, ys, zs):
	bestW = 0
	bestB = 0
	bestError = 100000000
	w = 100
	b = 100
	while w > -100:
		while b > -100:
			# print(w,b)
			currError = 0
			for i in range(len(xs)):
				currError += (zs[i] - g(w, b, xs[i], ys[i])) ** 2
			# print(w,b,currError)
			if(currError < bestError):
				bestError = currError
				bestW = w
				bestB = b
				print(bestW, bestB, currError)
			b -= .1
		b = 100
		w -= .1