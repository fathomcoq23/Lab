#bubblesort.py

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

swap = False
swap_count = 0
while not swap:
    swap = True
    for j in range(1,n):
        if a[j-1] > a[j]:
            swap = False
            swap_count += 1
            temp = a[j]
            a[j] = a[j-1]
            a[j-1] = temp

print("Array is sorted in %d swaps."%swap_count)
print("First Element: %d" %a[0])
print("Last Element: %d" %a[n-1])
