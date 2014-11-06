#-------------------------------------------------------------------------------
# Name:         fibonacciIII
# Purpose:      Use four techniques for Fibonacci
#
# Author:      Rushi Shah
#
# Created:     24/10/2014
# Copyright:   (c) Rushi Shah 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def fib1(n):
    if(n<3):
        return 1
    else:
        a = 1; b = 1;
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return c
def fib2(n):
    if n<3: return 1
    else: return (fib2(n-1) + fib2(n-2))
def fib3(n):
    if(n<3):
        return 1
    else:
        a = 1; b = 1;
        for i in range(2, n):
            b, a = a+b, b
        return b
def fib4(n):
    lookup = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    if n<12: return lookup[n-1]
    else: return (fib2(n-1) + fib2(n-2))
def fib5(n):
    return [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144][n-1]

def fib6(n):
    dictionary = {1:1, 2:1}
    if(n in dictionary): return dictionary[n]
    else:
        dictionary[n] = fib6(n-1) + fib6(n-2)
        return dictionary[n]
def fib7(n):
    #Binet's formula?
    from math import sqrt, floor
    return floor((pow((1+sqrt(5)), n) - pow((1-sqrt(5)), n))/((pow(2, n)*sqrt(5))))
def fib8(n):
    from decimal import Decimal, getcontext
    from math import sqrt
    if n>70:
        getcontext().prec = 2*n
    return (pow((1+sqrt(5)), n) - pow((1-sqrt(5)), n))/((pow(2, n)*sqrt(5)))




def main():
    from time import clock
    start = clock()
    n = int(input("Fibbonacci number?"))
    print("Ans 1", fib1(12))
    print('   time = ', round(clock()-start,1), 'seconds')

    start = clock()
    print("Ans 2", fib2(12))
    print('   time = ', round(clock()-start,1), 'seconds')

    start = clock()
    print("Ans 3", fib3(n))
    print('   time = ', round(clock()-start,1), 'seconds')

    start = clock()
    print("Ans 4", fib4(n))
    print('   time = ', round(clock()-start,1), 'seconds')

    start = clock()
    print("Ans 5", fib5(n))
    print('   time = ', round(clock()-start,1), 'seconds')

    start = clock()
    print("Ans 6", fib6(n))
    print('   time = ', round(clock()-start,1), 'seconds')

    start = clock()
    print("Ans 7", fib7(n))
    print('   time = ', round(clock()-start,1), 'seconds')

    start = clock()
    print("Ans 8", fib8(n))
    print('   time = ', round(clock()-start,1), 'seconds')


if __name__ == '__main__':
    main()
