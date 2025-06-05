n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
low = 0
high = (max(a)- min(a))/min(b)
ans = high
from math import log2
def check(m):
    left = float("-inf")
    right = float("inf")
    for i in range(n):
        temp1 = a[i] - (m*b[i])
        temp2 = a[i] + (m*b[i])
        left = max(left, temp1)
        right = min(right, temp2)
    return left<=right


while high - low >= 0.000001:
    mid = (low + high) / 2
    if check(mid) :
        ans = min(ans, mid)
        high = mid 
    else:
        low = mid
print(ans)
