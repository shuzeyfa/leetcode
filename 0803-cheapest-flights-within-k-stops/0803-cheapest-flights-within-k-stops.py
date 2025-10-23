class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        d = defaultdict(list)
        for u, v, w in flights:
            d[u].append((w, v))
        
        heap= [(0, src, 0)]
        min_step = {node:float("inf") for node in range(n)}
        min_step[src] = 0

        while heap:
            cur, node, step = heappop(heap)

            if node == dst:
                return cur
            
            if step > k:
                continue
            
            if step > min_step[node]:
                continue

            min_step[node] = step

            for weight, nei in d[node]:
                heappush(heap, (weight+cur, nei, step + 1))
 
        return -1
 