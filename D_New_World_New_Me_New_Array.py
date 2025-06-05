import math
for _ in range(int(input())):
    n, k, p=map(int,input().split())
    if n*p<abs(k):
        print(-1)
    else:
        print(math.ceil(abs(k)/p))