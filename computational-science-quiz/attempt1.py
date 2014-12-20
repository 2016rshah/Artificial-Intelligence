#-------------------------------------------------------------------------------
# Name:         Computational Science
# Purpose:      Practicing Computational Science
#
# Author:      Rushi Shah
#-------------------------------------------------------------------------------

#Variables
from random import randint 
from time import clock
start = clock()
cupboard = [
	[1, 1],
	[1, 0],
	[0, 0]
] #1: gold, 0: silver
failures = 0
successes = 0
trials = True
numTrials = 100000


#All trials
while(trials):
	chest = cupboard
	i = randint(0, 2)
	j = randint(0, 1)
	coin = chest[i][j]
	if(coin == 1):
		if(j == 1):
			newCoin = chest[i][0]
		else:
			newCoin = chest[i][1]
		if(newCoin == 1):
			successes += 1
		else:
			failures +=1
	if(successes + failures > numTrials):
		trials = False


#Printing results and time
print("Number of trials", numTrials)
print("Successes", successes)
print("Failures", failures)
print("Success ratio: ", successes/numTrials)
print('   time = ', round(clock()-start,1), 'seconds')