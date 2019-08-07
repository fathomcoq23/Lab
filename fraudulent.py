#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the activityNotifications function below.
def activityNotifications(s, d,n_day):
    day_limit = (2*(10**5))
    if n_day <= (day_limit) :
        notification = 0
        i = 0
        while i < n_day and d<n_day:
            #data to be used to determin if the client show revieve a notification
            data= s[i:d] #sublist to finding median
            data.sort()
            if (len(data)) %2 ==0 : # #the list elements is from position i to
                m = len(data)//2 #werde to start from to calculate median
                median = (sum(data[m-1:m+1])//2)
                if s[m+2]>= (2*median) and (len(s) -(len(data))) > 1:
                    notification+= 1
                else:
                    pass

            else:
                size_1 = len(data)
                div = size_1 // 2
                n = size_1-div
                median = data[n-1]

                if s[n+2] >= (2*median):
                    notification+= 1
                else:
                    pass
            i+= 1
            d+= 1

        return notification

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n_day = int(nd[0])

    d = int(nd[1])

    s = list(map(int, input().rstrip().split()))

    result = activityNotifications(s, d,n_day)

    fptr.write(str(result) + '\n')

    fptr.close()
