from bisect import bisect_right
from fractions import Fraction
for _ in range(int(input())):
    n,k,q=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    speed = []
    for i in range(k):
        if i == 0:
            speed.append(Fraction(a[i], b[i]))
        else:
            val1 = a[i] - a[i-1]
            val2 = b[i] - b[i-1]
            speed.append(Fraction(val1, val2))
    ans = []
    for i in range(q):
        n = int(input())
        ind = bisect_right(a,n)
        if ind == 0:
            ans.append(int(Fraction(n,speed[0])))
        else:
            tot = b[ind-1]
            if n>a[ind-1]:
                rem = n - a[ind-1]
                tot += (Fraction(rem,speed[ind]))
            ans.append(int(tot))
        
    print(*ans)