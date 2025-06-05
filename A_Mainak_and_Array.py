for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    maxx = 0
    if n == 1:
        print(0)
    else:
        for  i in range(1,n):
            maxx = max(l[i]-l[0],maxx)
        for i in range(n-2,-1,-1):
            maxx = max(maxx,l[n-1]- l[i])
        for i in range(n-1):
            maxx = max(l[i]-l[i+1],maxx)
        print(maxx)
            