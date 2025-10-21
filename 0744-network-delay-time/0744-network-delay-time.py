class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        

        d = defaultdict(set)
        graph = [i for i in range(1, n+1)]
        
        for u, v, w in times:
            d[u].add((v, w))
            


        distance = {node: float("inf") for node in graph}
        distance[k] = 0

        heap = [(0, k)]

        while heap:
            dist, node = heappop(heap)

            if dist > distance[node]:
                continue
            
            for nei, weight in d[node]:
                length = dist + weight

                if length < distance[nei]:
                    distance[nei] = length
                    heappush(heap, (length, nei))
        
        ans = 0
        # print(distance)
        for i in distance:
            if distance[i] == float("inf"):
                return -1
            ans = max(distance[i], ans)
        return ans
