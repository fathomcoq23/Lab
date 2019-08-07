#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    i =1
    j = " "

    while (n != 0):
        print(j*(n-1) + "#"*i)
        i+=1
        n-=1

if __name__ == '__main__':
    n = int(input())

    staircase(n)
