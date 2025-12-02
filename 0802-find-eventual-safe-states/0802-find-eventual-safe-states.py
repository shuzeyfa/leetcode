class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        deg = [0]*len(graph)
        d = defaultdict(list)
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                d[graph[i][j]].append(i)

        for i in range(len(graph)):
            deg[i] += len(graph[i])
        
        q = deque()
        for i in range(len(graph)):
            if len(graph[i]) == 0:
                q.append(i)
        ans = []
        while q:
            cur = q.popleft()
            ans.append(cur)

            for i in d[cur]:
                deg[i] -= 1
                if deg[i] == 0:
                    q.append(i)
        ans.sort()
        return ans
