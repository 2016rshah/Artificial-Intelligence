#-------------------------------------------------------------------------------
# Name:        Create Dictionary
# Purpose:      For use with the Railroad project
#
# Author:      Rushi Shah
#
# Created:     10/7/2014
#-------------------------------------------------------------------------------
def readWordFile(fileName):

    print("Lines in file: " + str(len(lines)))
    return lines

def createCityDict(lines):
    dictionary = {}
    for line in lines:
        words = line.split(" ")
        dictionary[words[0]] = [words[1]]
    return dictionary

def appendLatLon(dictionary, lines):
    temp = {}
    for line in lines:
        words = line.split(" ")
        temp[words[0]] = [words[1], words[2]]
    for key in dictionary:
        dictionary[key].append(temp[key])
    return dictionary

def dictToFile(dict):
    dictionary = open("railsDictionary.txt", "wb")
    import pickle
    pickle.dump(dict, dictionary)
    dictionary.close()


def createEdgeDict():
    file = open(fileName, "r")
    lines = file.readlines()
    for index in range(len(lines)):
        lines[index] = lines[index].strip()

def main():
    cities = readWordFile("rrNodeCity.txt")
    cityDict = createCityDict(cities)
    latlon = readWordFile("rrNodes.txt")
    cityDict = appendLatLon(cityDict, latlon)
    print(cityDict)
    dictToFile(cityDict)

from time import clock
START_TIME = 0
START_TIME = clock()

main()

print('+===<RUN TIME>===+')
print('| %5.2f'%(clock()-START_TIME), 'seconds |')
print('+================+')
