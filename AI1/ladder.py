#---------------------------------------------------------------+
# Name:     Ladder Lab Attempt 1                                |
# Purpose:  Find a path from two words using their neighbours   |
# Author:   Rushi Shah                                          |
# Created:  12/09/2014                                          |
#---------------------------------------------------------------+
#Global variables
dictionary = {}
#---------------------------------------
def createDictionary():
    global dictionary
    file = open("dictionary.txt", "rb")
    import pickle
    dictionary = pickle.load(file)
    file.close()
    return dictionary
#--------------------------------------
def findPath(current, target, visited = []):
    global dictionary
    assert type(dictionary) == dict, "not a dictionary"
    if(current != target and current not in visited):
        visited.append(current)
        nbs = dictionary[current]
        for nb in nbs:
            temp = list(visited)
            findPath(nb, target, temp)
    elif(current == target):
        visited.append(current)
        print(visited)
        exit()
#--------------------------------------
def main():
    global dictionary
    dictionary = createDictionary()
    initial = input("Initial word: ")
    target = input("Target word: ")
    array = []
    findPath(initial, target)
    print("Path not found")
main()
