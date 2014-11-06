"""
#---------------------------------------------------------------+
# Name:     Ladder Lab Attempt 3                                |
# Purpose:  Find a path from two words using their neighbours   |
# Author:   Rushi Shah                                          |
# Created:  12/09/2014                                          |
#---------------------------------------------------------------+
"""
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
def printPath(path, pops, maxLenQ, printStats = True):
    print(path)
    if(printStats):
        print("Pops = "+str(pops))
        print("Max length of the queue = " + str(maxLenQ))
        print("Path length= " + str(len(path)))
    exit()
#--------------------------------------
def iterative(initial, target, children, parents):
    closed = {}
    pops = 0
    maxLenQ = 0
    visited = []
    q = []
    dist = (lambda word: sum([target[n] != word[n] for n in range(0, 6)]))
##  f-value (g+h), word, path, g
    q.append([dist(initial), initial, [initial], 0])
    while(len(q) != 0):
        current = q.pop(0)
        pops+=1
        if(current[1] == target):
            printPath(current[2], pops, maxLenQ)
        closed[current[1]] = current[3]
        for word in children[current[1]]:
##create child regardless
            path = list(current[2])
            path.append(word)
            depth = len(current[2])+1
            newChild = [dist(word)+depth, word, path, depth]

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
#--------------------------------------
def main():
    children = createDictionary()
    words = getWordInput()
    parents = {}
    parents[words[0]] = "None"
    iterative(words[0], words[1], children, parents)
main()