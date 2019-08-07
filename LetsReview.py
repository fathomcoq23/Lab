# Enter your code here. Read input from STDIN. Print output to STDOUT

#letsReview.py

#number of strings
n = int(input())
for i in range(n):
    string_even =""
    string_odd = ""
    string = str(input())
    for j in range(len(string)):
        if j%2 == 0:
            string_even += string[j]
        else:
            string_odd += string[j]
    string = string_even +" "+  string_odd
    print(string)
