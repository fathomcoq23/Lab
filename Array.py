#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    string = ""
    arr = list(map(int, input().rstrip().split()))
    i = len(arr)-1
    while i >= 0:
        string += str(arr[i])
        string += " "
        i-=1
    print(string)

