# Enter your code here. Read input from STDIN. Print output to STDOUT

#probability
import itertools

n = int(input())
string = list(map(str,(input().rstrip().split(" "))))

pos = int(input().rstrip())
list_ = list(itertools.combinations(string,pos))
count = 0
for i in list_:
    if string[pos-1] in i:
        count += 1
print("%.12f" %(count/len(list_)))
