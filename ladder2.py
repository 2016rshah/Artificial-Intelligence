#---------------------------------------------------------------+
# Name:     Ladder Lab Attempt 2                                |
# Purpose:  Find a path from two words using their neighbours   |
# Author:   Rushi Shah                                          |
# Created:  12/09/2014                                          |
#---------------------------------------------------------------+
#Global variables
children = {}
parents = {}
visited = []
#---------------------------------------
def createDictionary():
    global children
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
def checkChildren(current, target):
    global children
    global parents
    if(current!=target and current not in visited):
        for word in children[current]:
            if(word not in parents):
                parents[word] = current
            if(word == target):
                printPath(word)
        visited.append(current)
    elif(current == target):
        printPath(current)
#--------------------------------------
def printPath(word):
    global parents
    path = []
    count = 0
    while(parents[word]!="None" and count<100):
        path.append(word)
        word = parents[word]
        count+=1
    path.append(word)
    path.reverse()
    print(path)
    exit()
#--------------------------------------
def findPath(current, target, currDepth, maxDepth):
    global children
    global parents
    if(currDepth<maxDepth):
        checkChildren(current, target)
        for child in children[current]:
            checkChildren(child, target)
        for child in children[current]:
            findPath(child, target) #SOMETHING ABOUT INCREASING DEPTH HERE!
#--------------------------------------
def iterative(initial, target):
    q = []
    q.append(initial)
    visited = []
    while(len(q) != 0):
        current = q.pop(0)
        visited.append(current)
        if(current == target):
            printPath(current)
        for word in children[current]:
            if(word not in parents):
                parents[word] = current
                q.append(word)
    print("path not found")
#--------------------------------------
def main():
    global children
    global parents
    children = createDictionary()
    words = getWordInput()
    parents[words[0]] = "None"
##    findPath(words[0], words[1])
    iterative(words[0], words[1])
    print("Path not found")
main()