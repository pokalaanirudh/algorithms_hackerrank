#!/bin/python3

import math
import os
import random
import re
import sys
res=[0,0]
# Complete the compareTriplets function below.
def compareTriplets(a, b):
    for i in range(3):
        if a[i]>b[i]:
               res[0]+=1
        elif a[i]==b[i]:
            continue   
        else:
            res[1]+=1
    return res        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
