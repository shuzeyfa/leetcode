from collections import defaultdict,deque
import heapq
n,m = map(int,input().split())
deg = [0 for i in range(n)]
d = defaultdict(list)
for i in range(m):
    u,v = map(int,input().split())
    d[u].append(v)
    deg[v-1]+=1
q=[]
for i in range(n):
    if deg[i] == 0:
        heapq.heappush(q,i+1)
ans = []
while q:
    cur = heapq.heappop(q)
    ans.append(cur)
    for i in d[cur]:
        deg[i-1]-=1
        if deg[i-1] == 0:
            heapq.heappush(q,i)
if len(ans) < n:
    print(-1)
else:
    print(*ans)
