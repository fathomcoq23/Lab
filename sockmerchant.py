import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count_total = 0
    ar.sort()
    for item in ar:
        count_item = ar.count(item)
        count_total += count_item // 2
        for i in range(1,count_item):
            ar.remove(item)

    return count_total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
