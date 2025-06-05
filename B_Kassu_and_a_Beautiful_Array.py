from bisect import bisect_left
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    odd = []
    even = []
    for i in l:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)

    even.sort()
    odd.sort()

    even_list = []

    for i in l:
        if i%2 == 0:
            even_list.append(1)
        else:
            val = bisect_left(odd,i)
            if val != 0:
                even_list.append(1)
    
    if len(even_list) == n:
        print("YES")
        continue

    odd_list = []

    for i in l:
        if i%2 == 1:
            odd_list.append(1)
        else:
            val = bisect_left(odd,i)
            if val != 0:
                odd_list.append(1)
    if len(odd_list) == n:
        print("YES")
    else:
        print("NO")
