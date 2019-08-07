if __name__ == '__main__':
    n = int(input())
    j = 0
    while j < n:
        integer_list = list(map(int, input().split()))
        j += 1

    i=1
    while(i <= n):
        integer_list.append(i)
        i+=1
        tup = tuple(integer_list)
    print(hash(tup))
