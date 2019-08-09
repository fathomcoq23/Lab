#exception handling
import sys

string = input().strip()

try: 
    print (int(string))
except ValueError: 
    print ("Bad String")
