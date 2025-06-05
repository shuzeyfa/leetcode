for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))

    maxx = max(l)
    t=False
    for i in range(n):
        if l[i] == maxx:
            if i == 0:
                if l[i+1] < l[i]:
                    print(i+1)
                    t = True
                    break
            elif i == n-1:
                if l[i-1] < l[i]:
                    print(i+1)
                    t = True
                    break
            else:
                if l[i-1] < l[i] or l[i+1] < l[i]:
                    print(i+1)
                    t = True
                    break
    if t == False:
        print(-1)