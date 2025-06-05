from collections import defaultdict,deque
n = int(input())
deg=[0]*n
d=defaultdict(list)
for i in range(n):
    val = int(input())
    if val == -1:
        continue
    else:
        deg[i] += 1
        d[val-1].append(i)
q = deque()
for i in range(n):
    if deg[i] == 0:
        q.append(i)
count = 0
while q:
    ind = len(q)
    for i in range(ind):
        cur = q.popleft()
        for i in d[cur]:
            deg[i] -= 1
            if deg[i]==0:
                q.append(i)
    count += 1
print(count)

