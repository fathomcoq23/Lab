#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):

    #find the maximum height.thats the height at which he can't blow off the candles
    max_height = max(ar)
    #counts the candles if can blow
    count = 0
    #for every height compare to max_height
    for i in ar:
        #if all the other heights are less than max_height
        if i == max_height:
            #count gets incremented
            count += 1
        else:
            pass
    return (count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
