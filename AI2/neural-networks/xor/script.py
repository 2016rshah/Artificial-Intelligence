from math import e
from random import random

NUM_TRIALS = 50

def sigmoid(x):
	'''squashing function'''
	return 1/(1 + e ** (-x))
def deriv(x):
	'''First derivative of squashing function'''
	return sigmoid(1 - sigmoid(x))

#list of list of weights
def calcFeedForward(weights, trainingSet):
	'''
	input of set of weights to test and training set
	training set: [([0,0],0), ([0,1],1)]
	weights: [w0,w1...w8]
	output of output at each node
	'''
	# print(trainingSet)
	inputs = list(trainingSet[0])
	expected = trainingSet[1]
	inputs.append(1) #bias
	# print(inputs, weights)
	x11 = sigmoid(dotProduct(inputs, weights[0]))
	# print(x11)
	x01 = sigmoid(dotProduct(inputs, weights[0]))
	# print(x01)
	x2 = sigmoid(dotProduct([x11,x01], weights[1]))
	# print(x2)
	out = dotProduct([x2], weights[2])

	# print(out)
	return [x11, x01, x2, out]
	# return [out, x2, x01, x11]

def dotProduct(inputs, weights):
	'''
	adder function
	sum the product of corresponding values
	weights is not same length as inputs, you need to select correct one
	'''
	# print(inputs, weights, startLoc)
	# dp = 0
	# for i in range(0, len(inputs)):
	# 	dp += inputs[i] * weights[i]
	# return dp
	return sum([inputs[i] * weights[i] for i in range(len(inputs))])

def corresProduct(xs, ys):
	return [x * y for x in xs for y in ys]

def calcGradient(ts, ws, vs):
	'''
	ts = trainingSet ([i1, i2], expectedOutput)
	weights (ws) and intermediate values (vs)
	'''
	# print(ts, ws, vs)
	gradients = []

	inputs, expected = ts
	[x11, x01, x2, out] = vs
	finalOut = vs[3]
	finalWeight = ws[2][0]
	error = expected - finalOut * finalWeight
	x2 = vs[2]
	gradient1 = error * x2
	gradients.append(gradient1)

	d = deriv(x2) # idk if this is the right value
	w = ws[2][0] # idk if this is the right value
	helper2 = error * w * d # in general, idk about this line
	gradient2 = x01 * helper2
	gradient3 = x11 * helper2
	gradients.append(gradient2)
	gradients.append(gradient3)

	helper3, helper4 = corresProduct(ws[1], [helper2])

	sixGradients = corresProduct([helper3, helper4], [inputs[0], inputs[1], 1])
	[gradients.append(x) for x in sixGradients]

	# print("gradients: ", gradients)
	return gradients

def applyGradientsToWeights(weights, gradients):
	alpha = .1
	ws0, ws1, ws2 = weights
	ws = ws0 + ws1 + ws2
	for i in range(len(ws)):
		ws[i] = ws[i] + (gradients[i] * alpha)
	ws = [ws[0:5], ws[5:7], ws[7:8]]
	# print("weights:",ws)
	return ws


def main():
	trainingSet = [([0,0],0), ([0,1], 1), ([1,0],1), ([1,1], 0)]
	# trainingSet = [([1,0],1)]
	weights = [[1 for x in range(6)], [1 for x in range(2)], [1 for x in range(1)]]	
	# bestError = 10000000
	# bestWeights = []
	for i in range(NUM_TRIALS):
		# weights = [[random()*2 - 1 for x in range(7)], [random()*2 - 1 for x in range(3)], [random()*2 - 1 for x in range(2)]]
		# weights = [[1 for x in range(6)], [1 for x in range(2)], [1 for x in range(1)]]
		currError = 0
		for j in range(len(trainingSet)):
			vs = calcFeedForward(weights, trainingSet[j])
			currValue = vs[len(vs)-1]
			currError += (currValue - trainingSet[j][1]) ** 2
			gs = calcGradient(trainingSet[j], weights, vs)
			weights = applyGradientsToWeights(weights, gs)
			# print(currError)
		
		# if(currError < bestError):
		# 	bestWeights = list(weights)
		# 	bestError = currError
		# 	print(bestError)
		print(i, currError)
			# gradient = calcGradient(weights)
			# applyGradientToWeights(weights, gradient)
	# print(bestError, bestWeights)
main()