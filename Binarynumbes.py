#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    list_ = []
    bin_list = []
    cons = []

    while (n != 0):
        m = n // 2
        remainder = n%2
        list_.append(remainder)
        n = m

    i = len(list_)-1
    while i >= 0:
        bin_list.append(list_[i])
        i-= 1


    count = 0
    for i in bin_list:
        if i == 1:
            count += 1
        else:
            cons.append(count)
            count = 0
        cons.append(count)

    print(max(cons))

