#-------------------------------------------------------------------------------
# Name:        New (and final I think) railroad lab
# Purpose:
#
# Author:      Rushi Shah
#
# Created:     16/10/2014
# Copyright:   (c) Rushi Shah 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
fullDict = {}
from math import pi , acos , sin , cos
def createDictionary():
    file = open("rrEdges.txt")
    lines = file.readlines()
    for index in range(len(lines)):
        lines[index] = lines[index].strip()
    dictionary = {}
    for line in lines:
        words = line.split(" ")
        if(words[0] in dictionary):
            dictionary[words[0]][0].append(words[1])
        else:
            dictionary[words[0]] = [[words[1]]]
    file = open("rrNodes.txt")
    lines = file.readlines()
    for index in range(len(lines)):
        lines[index] = lines[index].strip()
    for line in lines:
        words = line.split(" ")
        if(words[0] in dictionary):
            dictionary[words[0]].append([words[1], words[2]])
    return dictionary

def printPath(path, pops, maxLenQ, printStats = True):
    print(path)
    if(printStats):
        print("Pops = "+str(pops))
        print("Max length of the queue = " + str(maxLenQ))
        print("Path length= " + str(len(path)))
    exit()

def dist(z1, z2, dictionary):
    y1 = dictionary[z1][1][0]
    x1 = dictionary[z1][1][1]
    y2 = dictionary[z2][1][0]
    x2 = dictionary[z1][1][1]
    #
    y1  = float(y1)
    x1  = float(x1)
    y2  = float(y2)
    x2  = float(x2)
    #
    R   = 3958.76 # miles
    #
    y1 *= pi/180.0
    x1 *= pi/180.0
    y2 *= pi/180.0
    x2 *= pi/180.0
    #
    # approximate great circle distance with law of cosines
    #
    return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R
    #

def findPath(initial, target, dictionary):
    closed = {}
    pops = 0
    maxLenQ = 0
    visited = []
    q = []
##  f-value (g+h), word, path, g
    q.append([dist(initial, target, dictionary), initial, [initial], 0])
    while(q):
        current = q.pop(0)
        pops+=1
        if(current[1] == target):
            printPath(current[2], pops, maxLenQ)
        closed[current[1]] = current[3]
        for word in dictionary[current[1]][0]:
            if(word in dictionary):
                ##create child regardless
                path = list(current[2])
                path.append(word)
                depth = len(current[2])+1
                newChild = [dist(word, target, dictionary)+depth, word, path, depth]
                ##if statements
                wordsInQ = []
                for item in q:
                    wordsInQ.append(item[1])
                if(closed.get(newChild[1]) and closed[newChild[1]] < newChild[3]):
                    pass
                elif(closed.get(newChild[1]) and closed[newChild[1]]>newChild[3]):
                    del closed[newChild[1]]
                    q.append(newChild)
                    if(len(q)>maxLenQ):
                        maxLenQ = len(q)
                elif(newChild[1] not in wordsInQ):
                    q.append(newChild)
                    if(len(q)>maxLenQ):
                        maxLenQ = len(q)
                for i in range(len(q)):
                    j = 1
                    if(q[i][j] == newChild[1]):
                        if(q[i][3]<newChild[3]):
                            pass
                        else:
                            q.remove(q[i])
                            q.append(newChild)
                            if(len(q)>maxLenQ):
                                maxLenQ = len(q)
                q.sort()
    print("Path not found")

def main():
    global fullDict
    fullDict = createDictionary() #fullDict[cityNum] = [[nb1, nb2], [lat, lon]]
    print("The dictionary has", len(fullDict), "keys")
    city1 = input("Departing city number?")
    city1 = city1.strip()
    city2 = input("Arriving city number?")
    city2 = city2.strip()
    findPath(city1, city2, fullDict)


if __name__ == '__main__':
    main()
