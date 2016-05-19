#Expected to use Python 3!!

from math import e

def f(w, b, x):
	return 1 / (1 + (e ** (-w * x + b)))

def g(w,b,x,y):
	return 1 / (1 + (e ** (-w * (x+y) + b)))

# NOT
# 0 -> 1
# 1 -> 0
def notHillClimbing():
	for w in range(100,0,-1):
		for b in range(100,0,-1):
			y0 = f(w,b,0)
			y1 = f(w,b,1)
			if(y0 < .1 and y1 > .9):
				print(w,b)
#I'm not sure if this is okay
def nnNot(x):
	if(f(6, 3, x) < .1):
		return 1
	else:
		return 0
#6 and 3 look pretty good

# AND
# 0 -> 0 -> 0
# 0 -> 1 -> 0
# 1 -> 0 -> 0
# 1 -> 1 -> 1
def andHillClimbing():
	for w in range(100,0,-1):
		for b in range(100,0,-1):
			y00 = g(w,b,0,0)
			y01 = g(w,b,0,1)
			y10 = g(w,b,1,0)
			y11 = g(w,b,1,1)
			if (y00 < .1 and y01 < .1 and y10 < .1 and y11 > .9):
				print(w,b)
#6 and 9 work okay

def nnAnd(x,y):
	if(g(6,9,x,y) < .5):
		return 0
	else:
		return 1

# OR
# 0 -> 0 -> 0
# 0 -> 1 -> 1
# 1 -> 0 -> 1
# 1 -> 1 -> 1
def orHillClimbing():
	for w in range(100,0,-1):
		for b in range(100,0,-1):
			y00 = g(w,b,0,0)
			y01 = g(w,b,0,1)
			y10 = g(w,b,1,0)
			y11 = g(w,b,1,1)
			if (y00 < .1 and y01 > .9 and y10 > .9 and y11 > .9):
				print(w,b)
#6 and 3 work okay

def nnOr(x,y):
	if(g(6,3,x,y) < .5):
		return 0
	else:
		return 1