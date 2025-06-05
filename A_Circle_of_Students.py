def check(l,n):
    t2=False
    for i in range(n):
        num = l[i:]+l[:i]
        t=True
        for j in range(1,n):
            if num[j] < num[j-1]:
                t=False
                break
        if t==True:
            t2=True
            break
    l.reverse()

    for i in range(n):
        num = l[i:]+l[:i]
        t=True
        for j in range(1,n):
            if num[j] < num[j-1]:
                t=False
                break
        if t==True:
            t2=True
            break
    
    return t2
        

for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    if check(l,n):
        print("YES")
    else:
        print("NO")