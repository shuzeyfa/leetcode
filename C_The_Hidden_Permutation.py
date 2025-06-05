from collections import defaultdict
import heapq
for _ in range(int(input())):
    n = int(input())
    l = []
    for i in range(n):
        l.append(input())

    deg = [0]*n
    d = defaultdict(list)

    for i in range(n):
        s = l[i]
        for j in range(n):
            if s[j] == "1":
                if i < j:
                    deg[j] += 1
                    d[i+1].append(j+1)
                else:
                    deg[i] += 1
                    d[j+1].append(i+1)

    q = []
    heapq.heapify(q)
    for i in range(n):
        if deg[i] == 0:
            heapq.heappush(q,-(i+1))

    ans=[]
    while q:
        cur = -1*heapq.heappop(q)
        ans.append(cur)
        for i in d[cur]:
            deg[i-1] -= 1
            if deg[i-1] == 0:
                heapq.heappush(q,-i)
    print(*ans)


