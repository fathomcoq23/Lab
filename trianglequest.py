#triangle.py

n = int(input())
for i in range(1,n+1):
    j = 1
    while(j <= i):
        print(j,end=" ")
        j += 1
    c = j-2
    while (c >= 1):
        print(c,end=" ")
        c-=1
    print("\n")
    
    
  either that or this 
  
for i in range(1,int(input())+1): 
  print(pow(((pow(10,i)-1)//9),2))
