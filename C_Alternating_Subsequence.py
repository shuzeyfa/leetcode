for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    res = []
    cur = l[0]

    for i in range(1,n):
        if (l[i] > 0 and cur >0) or (l[i] < 0 and cur < 0):
            cur = max(cur, l[i])
        else:
            res.append(cur)
            cur = l[i]
    res.append(cur)
    print(sum(res))
                
