for _ in range(int(input())):
    n ,k=map(int,input().split())
    summ = 0
    for i in range(n):
        w,h = map(int,input().split())
        summ += max(w,h)
    if summ >= k:
        print("YES")
    else:
        print("NO")