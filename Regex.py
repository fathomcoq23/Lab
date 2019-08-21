#!/bin/python3
#givinng a list of email addresses, scan and search for all gmail emails. if found print the names of all users in sorted other

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    list_gmail = []
    N = int(input())
    pattern = r"@gmail"
    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        if re.search(pattern,emailID):
            list_gmail.append(firstName)
        else:
            pass
    list_gmail.sort()
    for i in list_gmail:
        print(i)
