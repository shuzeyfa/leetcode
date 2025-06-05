from collections import defaultdict
n = int(input())
d = defaultdict(int)
for i in range(n):
    pos,dis = map(int,input().split())
    d[pos] = dis + pos
t = "NO"

for i in d:
    if d[i] in d:
        val = d[i]
        if d[val] == i:
            t="YES"
            break
print(t)

