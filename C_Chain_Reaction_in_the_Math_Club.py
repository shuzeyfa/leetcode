from collections import defaultdict,deque
n, m = map(int,input().split())
deg = [0]*n
d = defaultdict(list)
for i in range(m):
    a,b = map(int,input().split())
    deg[a-1] += 1
    deg[b-1] += 1
    d[a-1].append(b-1)
    d[b-1].append(a-1)


q = deque()
for i in range(n):
    if deg[i] == 1:
        q.append(i)

ans = []
count=0
while q:
    count += 1
    s = set()
    for i in range(len(q)):
        cur = q.popleft()
        
        for j in d[cur]:
            deg[j]-=1
            s.add(j)

    for j in s:
        if deg[j] == 1:
            q.append(j)  
print(count)
        

