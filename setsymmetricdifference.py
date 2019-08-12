# Enter your code here. Read input from STDIN. Print output to STDOUT

n_english = int(input().rstrip())
list_english = list(map(int,input().rstrip().split(" ")))
n_french = int(input().rstrip())
list_french = list(map(int,input().rstrip().split(" ")))

s = set(list_english).symmetric_difference(set(list_french))
print(len(s))
