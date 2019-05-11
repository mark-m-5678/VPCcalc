# -- Import --
import time
import os
import math

# -- Definitions --
def cls():
    os.system('cl' if os.name == 'nt' else 'clear')
    return

def isPos(n):
    try:
        math.factorial(n)
        return True
    except ValueError:
        return False

def canGetFact(n, k):
    try:
        C = (math.factorial(n))/(math.factorial(k)*math.factorial(n-k))
        return True
    except ValueError:
        return False

def getVar(n, k):
    #  FORMULA:
    #        n!
    # P =  ------
    #      (n-k)!
    #
    # Calculate V:
    V = (math.factorial(n))/(math.factorial(n-k))
    return V

def getPerm(n):
    # FORMULA:
    # P = n!
    #
    # Calculate P:
    P = math.factorial(n)
    return P

def getComb(n, k):
    #    FORMULA:
    #        n!
    # C = ---------
    #      k!(n-k)!
    #
    # Special cases where we don't need to calculate C:
    if k == 1:
        C = n
    elif k == 0:
        C = 1
    elif n == k:
        C = 1
    else:
        # TODO
        # This is probably stupid, but I don't know how to improve it and this just works
        # Maybe incorporate try/except directly into the main function...
        nPos = isPos(n)
        kPos = isPos(k)
        if nPos and kPos:
            fact = canGetFact(n, k)
            if fact:
                C = (math.factorial(n))/(math.factorial(k)*math.factorial(n-k))
            else:
                C = ("n must be larger than k")
        else:
            C = ("n and k can't be negative")
    return C

# -- Start --
# TODO - add a welcome message
while True:
    print('1. - Variations')
    print('2. - Permutations')
    print('3. - Combinations')
    print("Q - Quit")
    opt = input('>>> ')
    if opt in ['1', '1.']:
        print('Variations')
        n = int(input('n = '))
        k = int(input('k = '))
        res = getVar(n, k)
        print(res)
    elif opt in ['2', '2.']:
        print('Permutations')
        n = int(input('n = '))
        res = getPerm(n)
        print(res)
    elif opt in ['3', '3.']:
        print('Combinations')
        n = int(input('n = '))
        k = int(input('k = '))
        res = getComb(n, k)
        print(res)
    elif opt in ['e', 'E', 'q', 'Q', 'quit', 'exit']:
        quit()
    else:
        print("An error message that makes sense")
