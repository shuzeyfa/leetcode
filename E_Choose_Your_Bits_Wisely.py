n, m =map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

c = []
for i in range(n):
    minn = float("inf")
    for j in b:
        val = a[i] & j
        minn = min(minn, val)
    c.append(minn)
ans = 0
for i in c:
    ans |= i

print(ans)
