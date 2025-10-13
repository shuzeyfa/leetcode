class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d=defaultdict(list)
        l = ["white" for _ in range(numCourses)]
        for i,j in prerequisites:
            d[j].append(i)

        def dfs(node):

            if l[node] == "grey":
                return False
            if l[node] == "black":
                return True

            l[node] = "grey"
            for i in d[node]:
                found2 = dfs(i)
                if not found2:
                    return False

            l[node] = "black"
            return True
        
        for child in range(numCourses):
            found = dfs(child)
            if not found:
                return False
        return True
