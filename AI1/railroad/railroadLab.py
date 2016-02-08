#-------------------------------------------------------------------------------
# Name:        RailRoad Lab
# Purpose:      To find the path from two cities
#
# Author:      Rushi Shah
#
# Created:     10/10/2014
#-------------------------------------------------------------------------------

from math import pi , acos , sin , cos
def calcd(y1,x1, y2,x2):
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
def createDictionary():
    file = open("railsDictionary.txt", "rb")
    import pickle
    dictionary = pickle.load(file)
    file.close()
    return dictionary

def main():
    dictionary = createDictionary();
    print(dictionary)
    #key: city name
    #dictionary[key][1] = [lat, lon]
    city1 = input("City1?")
    city2 = input("City2?")
    print(calcd(dictionary[city1][1][0], dictionary[city1][1][1], dictionary[city1][1][0], dictionary[city2][1][0]))
main()


