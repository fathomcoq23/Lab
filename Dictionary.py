# Enter your code here. Read input from STDIN. Print output to STDOUT

#phonebook.py
phonebook = {}

n = int(input())
if n <= (10**5):
    for i in range(n):
        contact = list(input().rstrip().split(" "))
        name = str(contact[0])
        number = int(contact[1])
        phonebook[name] = number
i = 1
while i <= n:
    query = str(input())
    if query in phonebook:
        print("{}={}" .format(query,phonebook[query]))
    else:
        print("Not found")
    i += 1

