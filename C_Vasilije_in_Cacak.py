for _ in range(int(input())):
    n ,k ,x =map(int,input().split())
    minn = (k*(k+1))//2
    maxx = (n*(n+1) // 2) -  ((n-k)*(n-k+1)//2)
    if x<=maxx and x>=minn:
        print("YES")
    else:
        print("NO")