class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        ind = [0]*n
        d = defaultdict(list)
        for u,v in edges:
            ind[v] += 1
            d[u].append(v)

        q = deque()
        for i in range(n):
            if ind[i]==0:
                q.append(i)

        temp = [set() for i in range(n)]
        while q:
            cur = q.popleft()
            
            for i in d[cur]:
                temp[i].update(temp[cur])
                temp[i].add(cur)
                ind[i] -= 1
                if ind[i] == 0:
                    q.append(i)
        ans = [sorted(list(x)) for x in temp]
        return ans