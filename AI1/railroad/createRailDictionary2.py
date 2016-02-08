#-------------------------------------------------------------------------------
# Name:        Create Dictionary 2
# Purpose:      For use with the Railroad project
#
# Author:      Rushi Shah
#
# Created:     10/7/2014
#-------------------------------------------------------------------------------

def readWordFile(fileName):
    file = open(fileName, "r")
    lines = file.readlines()
    for index in range(len(lines)):
        lines[index] = lines[index].strip()
    print("Lines in file: " + str(len(lines)))
    return lines

def createNumToCityDictionary(lines):
    dictionary = {}
    for line in lines:
        words = line.split(" ")
        dictionary[words[0]] = [words[1]]
    return dictionary

def createCityToNumDictionary(lines):
    dictionary = {}
    for line in lines:
        words = line.split(" ")
        dictionary[words[1]] = [words[0]]
    return dictionary

def createCityToCoordDictionary(numToCity, cityToNum, lines):
    temp = {}
    for line in lines:
        numlatlon = line.split(" ")
        temp[numlatlon[0]] = [numlatlon[1], numlatlon[2]]
    #temp is numToCoord
    cityToCoord = {}
    for city in cityToNum:
        print(city)
        numOfCity = cityToNum[city]
        print(numOfCity)
        latlon = temp[numOfCity[0]]
        cityToCoord[city] = [latlon[0], latlon[1]]
    return cityToCoord

def dictToFile(dict):
    dictionary = open("railsDictionary.txt", "wb")
    import pickle
    pickle.dump(dict, dictionary)
    dictionary.close()

def main():
    cities = readWordFile("rrNodeCity.txt")
    numToCityDictionary = createNumToCityDictionary(cities)
    print(numToCityDictionary)
    cityToNumDictionary = createCityToNumDictionary(cities)
    print(cityToNumDictionary)
    latlon = readWordFile("rrNodes.txt")
    cityToCoordDictionary = createCityToCoordDictionary(numToCityDictionary, cityToNumDictionary, latlon)
    print(cityToCoordDictionary)
    dictToFile(cityToCoordDictionary)

from time import clock
START_TIME = 0
START_TIME = clock()

main()

print('+===<RUN TIME>===+')
print('| %5.2f'%(clock()-START_TIME), 'seconds |')
print('+================+')
