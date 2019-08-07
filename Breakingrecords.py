#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(score):
    low = score[0]
    high = score[0]
    count_high = 0
    count_low = 0

    for i in score:
        if i > high:
            count_high +=1
            high = i
        elif i == high:
            count_high = count_high
            high = i
        else:
            pass
        if i < low:
            count_low += 1
            low = i
        elif i == low:
            count_low = count_low
            low = i
        else:
            pass
    return (count_high,count_low )

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    score = list(map(int, input().rstrip().split()))

    result = breakingRecords(score)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
