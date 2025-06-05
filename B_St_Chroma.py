for _ in range(int(input())):
    n, k =map(int,input().split())
    if k>=n:
        print(*[x for x in range(n)])
    else:
        l = []
        for i in range(n):
            if i!=k:
                l.append(i)
        l.append(k)
        print(*l)