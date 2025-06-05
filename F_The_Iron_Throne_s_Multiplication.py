n, m, k = map(int,input().split())

def check(val):
    count = 0
    for i in range(1,n+1):
        count += min(val//i, m)
    return count >= k

low =  1
high = n*m
res = high
while low <= high:
    mid = (low + high) // 2
    if check(mid):
        res = mid
        high = mid - 1
    else:
        low = mid + 1
print(res)