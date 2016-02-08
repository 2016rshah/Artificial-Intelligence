"""
#---------------------------------------------------------------+
# Name:     Ladder Lab Attempt 3                                |
# Purpose:  Find a path from two words using their neighbours   |
# Author:   Rushi Shah                                          |
# Created:  12/09/2014                                          |
#---------------------------------------------------------------+
"""
def calcd(y1, x1, y2, x2):
    y1 = float(y1)
    x1 = float(x1)
    y2 = float(y2)
    x2 = float(x2)

    R = 3958.76 #miles
    y1 *= pi/180.0


def createDictionary():
    file = open("dictionary.txt", "rb")
    import pickle
    children = pickle.load(file)
    file.close()
    return children
#--------------------------------------
def getWordInput():
    initial = ""
    while(len(initial)!=6):
        initial = input("Initial word: ")
    target = ""
    while(len(target)!=6):
        target = input("Target word: ")
    result = [initial, target]
    return result
#--------------------------------------
def printPath(word, pops, maxLenQ, parents):
    path = []
    while(parents[word]!="None"):
        path.append(word)
        word = parents[word]
    path.append(word)
    path.reverse()
    print(path)
    print("Pops = "+str(pops))
    print("Max length of the queue = " + str(maxLenQ))
    print("Length of path = " + str(len(path)))
    exit()
#--------------------------------------
def iterative(initial, target, children, parents):
    pops = 0
    maxLenQ = 0
    visited = []
    q = []
    q.append(initial)
    while(len(q) != 0):
        dist = (lambda word: sum([target[n] != word[n] for n in range(0, 6)]))
        q.sort(key = dist)
        current = q.pop(0)
        pops+=1
        visited.append(current)
        if(current == target):
            printPath(current, pops, maxLenQ, parents)
        for word in children[current]:
            if(word not in parents):
                parents[word] = current #check if the g value is shorter
                q.append(word) #check if the g value is shorter
                if(len(q)>maxLenQ):
                    maxLenQ = len(q)
    print("Path not found")
#--------------------------------------
def main():
    children = createDictionary()
    words = getWordInput()
    parents = {}
    parents[words[0]] = "None"
    iterative(words[0], words[1], children, parents)
main()