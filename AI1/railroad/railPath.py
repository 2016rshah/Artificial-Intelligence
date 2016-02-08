"""
#---------------------------------------------------------------+
# Name:     Rail Lab Attempt 4                                  |
# Purpose:  Find a path between cities                          |
# Author:   Rushi Shah                                          |
# Created:  12/09/2014                                          |
#---------------------------------------------------------------+
"""
children = ""
latlon = ""
def getNumInput():
    initial = ""
##    while(len(initial)!=7):
    initial = input("Initial city number: ")
    target = ""
##    while(len(target)!=7):
    target = input("Final city number: ")
    result = [initial, target]
    return result
#--------------------------------------
def printPath(path, pops, maxLenQ, latlon, printStats = True):
    print(path)
    if(printStats):
        distance = 0
        for index in range(len(path)-1):
            distance+=dist(path[index], path[index+1], latlon)
        print("Distance between cities = ", distance)
        print("Pops = "+str(pops))
        print("Max length of the queue = " + str(maxLenQ))
        print("Path length= " + str(len(path)))
    exit()
#--------------------------------------
from math import pi , acos , sin , cos
def dist(z2, z1, latlon, count=0):
    if(z1 == z2):
        return 0
    y1 = latlon[z1][0]
    x1 = latlon[z1][1]
    y2 = latlon[z2][0]
    x2 = latlon[z2][1]
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
def iterative(initial, target, children, parents, latlon):
    closed = {}
    pops = 0
    maxLenQ = 0
    visited = []
    q = []
##  f-value (g+h), word, path, g
    q.append([dist(initial, target, latlon), initial, [initial], 0])
    while(len(q) != 0):
        current = q.pop(0)
        pops+=1
        if(current[1] == target):
            printPath(current[2], pops, maxLenQ, latlon)
        closed[current[1]] = current[3]
        if(current[1] in children):
            for word in children[current[1]]:
    ##create child regardless
                path = list(current[2])
                path.append(word)
                depth = len(current[2])+1
                newChild = [dist(word, target, latlon)+depth, word, path, depth]

    ##if statements

                wordsInQ = []
                for item in q:
                    wordsInQ.append(item[1])
                if(closed.get(newChild[1]) and closed[newChild[1]] > newChild[3]):
                    pass
                elif(closed.get(newChild[1]) and closed[newChild[1]]<newChild[3]):
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
                        if(q[i][3]>newChild[3]):
                            pass
                        else:
                            q.remove(q[i])
                            q.append(newChild)
                            if(len(q)>maxLenQ):
                                maxLenQ = len(q)
                q.sort()
    print("Path not found")
def createEdgeDictionary():
    file = open("rrEdges.txt")
    lines = file.readlines()
    for index in range(len(lines)):
        lines[index] = lines[index].strip()
    dictionary = {}
    for line in lines:
        words = line.split(" ")
        if(words[0] in dictionary):
            dictionary[words[0]].append(words[1])
        else:
            dictionary[words[0]] = [words[1]]
        if(words[1] in dictionary):
            dictionary[words[1]].append(words[0])
        else:
            dictionary[words[1]] = [words[0]]
    return dictionary
def createLatLonDictionary():
    file = open("rrNodes.txt")
    lines = file.readlines()
    for index in range(len(lines)):
        lines[index] = lines[index].strip()
    dictionary = {}
    for line in lines:
        words = line.split(" ")
        dictionary[words[0]] = [words[1], words[2]]
    return dictionary

#--------------------------------------
def main():
    global children
    global latlon
    children = createEdgeDictionary()
    latlon = createLatLonDictionary()
    words = getNumInput()
    parents = {}
    parents[words[0]] = "None"
    iterative(words[0], words[1], children, parents, latlon)
main()
