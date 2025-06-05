from math import gcd
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    even = []
    odd = []
    for i in l:
        if i % 2 == 1:
            odd.append(i)
        else:
            even.append(i)
    odd.sort(reverse=True)
    even += odd
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if gcd(even[i],2*even[j]) > 1:
                ans += 1
    print(ans)