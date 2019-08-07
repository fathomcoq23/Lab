#symmetric difference
#set one
num_1= int(input())
list_1 = list(map(int, input().rstrip().split()))
set_1 = set(list_1)

#set two
num_2 = int(input())
list_2 = list(map(int,input().rstrip().split()))
set_2 = set(list_2)


intersect = set_1.intersection(list_2)

difference_1 = set_1 - intersect
difference_2 = set_2 - intersect
l = list(difference_1.union(difference_2))
l.sort()

for i in l:
    print(i)
