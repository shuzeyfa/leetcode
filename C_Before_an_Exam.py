d, n =map(int,input().split())
l = []
l2 = []
for i in range(d):
    minn,maxx = map(int,input().split())
    l.append([minn,maxx])
    l2.append(minn)
    n -= minn
if n<0:
    print("NO")
elif n == 0:
    print("YES")
    print(*l2)
else:
    for i in range(d):
        dif = l[i][1] - l[i][0]
        if dif>=n:
            l2[i] += n
            n = 0
            break
        else:
            l2[i] += dif
            n -= dif
    if n == 0:
        print("YES")
        print(*l2)
    else:
        print("NO")
