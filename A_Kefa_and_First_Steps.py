n = int(input())
l = list(map(int,input().split()))
if n == 1:
    print(1)
elif n== 2:
    if l[0]<=l[1]:
        print(2)
    else:
        print(1)
else:
    left = 0
    maxx = 0
    for right in range(1,n):
        if l[right] < l[right-1]:
            left = right
        maxx = max(maxx, right - left + 1)
    print(maxx)
