__author__ = 'Nick'

import math

list = [2, 10, 11, 4, 9, 15, 20]

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def isSorted(l):
    prev = l[0]
    for x in l:
        if x >= prev:
            prev = x
            continue
        else:
            return False
    return True

def QuickSort(l):
    print('####### SORTING #######')
    print(l)

    high = []
    low = []

    while True:
        med = l[math.floor(len(l)/2)]
        print(med)
        for x in l:
             high.append(x) if x >= med else low.append(x)

        print(low)
        print(high)

        if isSorted(low + high):
            return low + high
        else:
            return QuickSort(low) + QuickSort(high)

slist = QuickSort(list)
print(slist)
