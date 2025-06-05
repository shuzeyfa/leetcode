import math
for _ in range(int(input())):
    n, k = map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    

    def check(val):
        val2 = 0
        for j in range(n):
            temp = math.ceil(a[j]/val)
            val2 += (temp*b[j])
        return val2<=k

    final = float("inf")
    low=1
    high = max(a)+1
    while low<=high:
        mid = (low+high)//2
        if check(mid):
            final = mid
            high = mid-1
        else:
            low=mid+1
    if final == float("inf"):
        print(-1)
    else:
        print(final)