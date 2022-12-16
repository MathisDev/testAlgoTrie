
from random import *

import math
import os
import random
import re
import sys

def trieInsertion(arr,n):
    for i in range(n):
        j = i - 1
        while (j >= 0 and arr[j] > arr[j + 1]):
            arr[j],arr[j+1] = arr[j+1],arr[j]
            j = j - 1
    return arr

def trieBulle(t,n):
    inversion = True
    while inversion:
        inversion = False
        for i in range(n-1):
            if t[i] > t[i + 1]:
                t[i],t[i + 1]=t[i + 1],t[i]
                inversion = True
    return t

def trieSelection(t,n):
    for i in range(n-1):
        posMin = i
        for j in range(i+1,n):
            if t[i] < t[posMin]:
                posMin = j
    return t
    


if __name__ == '__main__':
    i = 0
    arr = []
    while i != 10000:
        arr.append(randrange(1000))
        i = i + 1

    n = len(arr)
    result = trieSelection(arr,n)

    print(result)

'''
Pour 10000 element :

trieInsersion 6,38s
trieBulle 12,59s
trieSelection 3,28s

'''