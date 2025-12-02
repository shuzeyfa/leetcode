class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        deg = [0]*numCourses
        d = defaultdict(list)

        for u,v in prerequisites:
            d[v].append(u)
            deg[u]+=1
        
        q = deque()
        for i in range(len(deg)):
            if deg[i] == 0:
                q.append(i)
        ans = []
        while q:
            cur = q.popleft()
            ans.append(cur)
            for i in d[cur]:
                deg[i] -= 1
                if deg[i] == 0:
                    q.append(i)
        
        if len(ans) != numCourses:
            return []
        return ans