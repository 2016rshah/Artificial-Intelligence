#-------------------------------------------------------------------------------
# Name:         Alphanumeric
# Purpose:      Puzzling
#
# Author:      Rushi Shah
#
# Created:     22/10/2014
# Copyright:   (c) Rushi Shah 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

##def main():
puzzle = input("Puzzle?") #'SEND + MORE == MONEY'
print("Puzzle: ", puzzle)
solutionFound = 0
puzzle = puzzle.upper()
from re import findall
words = findall('[A-Z]+', puzzle)
keys = ''.join(set(''.join(words)))
from itertools import permutations
for values in permutations('1234567890', len(keys)):
    table = str.maketrans(keys, ''.join(values))
    equation = puzzle.translate(table)
    words = equation.split(" ")
    sw0 = False
    for word in words:
        if(word[0] == "0"):
            sw0 = True
    if(sw0):
        continue
    #print(equation)
    if(eval(equation)):
        print("---", equation)
        solutionFound +=1
        if(solutionFound > 2):
            exit()
if not solutionFound:
    print("No solutions have been found.")
else:
    print("All solutions have been found.")
input("okay?")
##if __name__ == '__main__':
##    main()
