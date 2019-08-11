import sys

class Solution:
     # Write your code here
    def __init__(self):
        self.stack = []
        self.queue = []
    #adding a character at the beginning
    def pushCharacter(self,c):
        self.stack.append(c)
    #append characters starting from the end
    def enqueueCharacter (self,c):
    #indexing from the last element in the giving string
        if c in s:
            i = s.index(c)
            i = (-i)-1
        self.queue.append(s[i])
    #removes a character from the stack list
    def popCharacter(self):
        char = self.stack.pop(i)
        return char
    #removes a character from the queue list
    def dequeueCharacter(self):
        char = self.queue.pop(i)
        return char

# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    
