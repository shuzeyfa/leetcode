# from collections import Counter
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    d={}
    for i in range(n):
        d[l[i]] = i
    
    maxx = minn = d[1]
    s=['0']*n
    s[0]="1"
    
    
    
    for i in range(2,n+1):
        ind = d[i]
        if ind<minn:
            minn = ind
        elif ind>maxx:
            maxx=ind
        if maxx-minn+1<=i:
            s[i-1] = "1"
        
    print("".join(s))