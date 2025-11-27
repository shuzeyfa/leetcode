class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        deg = [0]*numCourses
        d = defaultdict(list)
        for u,v in prerequisites:
            d[u].append(v)
            deg[v] += 1
        q=deque()
        for i in range(numCourses):
            if deg[i] == 0:
                q.append(i)
        temp = [set() for i in range(numCourses)]
        # print(d)
        while q:
            cur = q.popleft()
            for i in d[cur]:
                temp[i].update(temp[cur])
                temp[i].add(cur)
                deg[i] -= 1
                if deg[i] == 0:
                    q.append(i)

        ans =[ ]
        for u,v in queries:
            if u in temp[v]:
                ans.append(True)
            else:
                ans.append(False)
        return ans