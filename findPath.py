def createDictionary():
    file = open("dictionary.txt", "rb")
    import pickle
    dictionary = pickle.load(file)
    file.close()

def recurse(dictionary, word1, target, visited):
    assert(word1 )
    if(word1!=target and word1 not in visited):
        array = dictionary[word1]
        for word in array:
            temp = list(visited)
            temp.append(word1)
            recurse(word, target, temp)
    elif(word1==target):
        print("path found")
        return visited

def findPath(dictionary):
    initial = input("Initial word: ")
    target = input("Target word: ")
    #list as parameter. Make copy of list every time. Once found print list. Get rid of visited
    visited = []
    return recurse(dictionary, initial, target, visited)

dictionary = createDictionary()
print(findPath(dictionary))
