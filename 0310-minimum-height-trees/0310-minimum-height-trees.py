class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        d = defaultdict(list)
        deg = [0]*n
        for u,v in edges:
            deg[u]+=1
            deg[v]+=1
            d[u].append(v)
            d[v].append(u)

        
        q = deque()
        for i in range(n):
            if deg[i] == 1:
                q.append(i)

        rem = n
        while rem > 2:
            rem -= len(q)
            for i in range(len(q)):
                cur = q.popleft()
                for j in d[cur]:
                    deg[j] -= 1
                    if deg[j] == 1:
                        q.append(j)
        return list(q)


