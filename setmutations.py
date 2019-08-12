# Enter your code here. Read input from STDIN. Print output to STDOUT

#number of elements in set A abnd its inputs
n_elements = int(input().rstrip())
A= set(map(int,input().rstrip().split(" ")))

#number other sets to perform mutations
n_other = int(input().rstrip())
#take in the operation and sets
total = 0
for i in range(n_other):
    o,e = input().split(" ")
    new_set = set(map(int,input().rstrip().split(" ")))
    if str(o).upper() == "INTERSECTION_UPDATE":
        A.intersection_update(new_set)
        #print(A)
    elif str(o).upper() == "UPDATE":
        A.update(new_set)
        #print(A)
    elif str(o).upper() == "DIFFERENCE_UPDATE":
        A.difference_update(new_set)
        #print(A)
    elif str(o).upper() == "SYMMETRIC_DIFFERENCE_UPDATE":
        A.symmetric_difference_update(new_set)
        #print(A)
    else:
        pass
print(sum(A))
