"""
+------------------------+
|Title: Create Dictionary|
|By: Rushi Shah          |
|Date: 9/9/14            |
|Creates a dictionary of |
|all the neighbours of   |
|a list of 5000 words    |
+------------------------+
"""
#------------------------------
def readWordFile(fileName):
    file = open(fileName, "r")
    lines = file.readlines()
    for index in range(len(lines)):
        lines[index] = lines[index].strip()
    print("Number of words: "+str(len(lines)))
    return lines
#------------------------------
def dist(word1, word2):
    count = 0
    for index in range(len(word1)):
        if(word1[index]!=word2[index]):
            count+=1
    return count
#------------------------------
def nbList(word1, lines):
    array = []
    for word2 in lines:
        if(dist(word1, word2) == 1):
            array.append(word2)
    return array
#-----------------------------
def createDictionary(lines):
    dictionary = {}
    for word in lines:
        dictionary[word] = nbList(word, lines)
    print("Dictionary length: "+str(len(dictionary)))
    return dictionary
#----------------------------
def dictToFile(dict):
    dictionary = open("dictionary.txt", "wb")
    import pickle
    pickle.dump(dict, dictionary)
    dictionary.close()
#---------------------------
def main():
    wordList = readWordFile("words.txt")
    dictionary = createDictionary(wordList)
    dictToFile(dictionary)

from time import clock
START_TIME = 0
START_TIME = clock()
main()
print('+===<RUN TIME>===+')
print('| %5.2f'%(clock()-START_TIME), 'seconds |')
print('+================+')
