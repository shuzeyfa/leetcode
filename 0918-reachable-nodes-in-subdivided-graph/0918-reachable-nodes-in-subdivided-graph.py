class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        d = defaultdict(list)
        for u, v, w in edges:
            d[u].append((w, v))
            d[v].append((w, u))
        
        dist = [float('inf')] * n
        dist[0] = 0
        heap = [(0, 0)]
        
        while heap:
            moves, node = heapq.heappop(heap)
            if moves != dist[node]:
                continue
            for weight, nei in d[node]:
                new_moves = moves + weight + 1
                if new_moves < dist[nei] and new_moves <= maxMoves:
                    dist[nei] = new_moves
                    heapq.heappush(heap, (new_moves, nei))
        
        ans = 0
        # Count fully reachable nodes
        for i in range(n):
            if dist[i] <= maxMoves:
                ans += 1
        
        # Count partial edges
        for u, v, w in edges:
            a = max(0, maxMoves - dist[u])
            b = max(0, maxMoves - dist[v])
            ans += min(w, a + b)
        
        return ans