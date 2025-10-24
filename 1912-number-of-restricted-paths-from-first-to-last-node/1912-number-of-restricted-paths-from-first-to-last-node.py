class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:

        dic = defaultdict(list)

        for u, v, w in edges:
            dic[u].append((w, v))
            dic[v].append((w, u))
        
        distance = {node:float("inf") for node in range(1, n+1)}
        distance[n] = 0

        heap = [(0, n)]

        while heap:
            value, node = heappop(heap)

            for cur, nei in dic[node]:
                dist = cur + value

                if dist < distance[nei]:
                    distance[nei] = dist
                    heappush(heap, (dist, nei))
        print(distance)

        MOD = 10**9 + 7
        
        memo = {}
        
        def dfs(node):
            if node == n:
                return 1
            if node in memo:
                return memo[node]
            
            total = 0
            for _, nei in dic[node]:
                if distance[node] > distance[nei]:  # restricted path condition
                    total += dfs(nei)
            memo[node] = total % MOD
            return memo[node]
        
        return dfs(1)