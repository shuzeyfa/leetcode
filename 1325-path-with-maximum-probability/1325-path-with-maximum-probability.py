class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        d = defaultdict(set)

        for i in range(len(edges)):
            a, b = edges[i]
            d[a].add((b, succProb[i]))
            d[b].add((a, succProb[i]))
        
        heap = [(-1, start_node)]

        s = set()
        s.add(start_node)

        distance = {node: 0.0 for node in range(n)}
        distance[start_node] = 1
        # print(distance)
        while heap:
            cur, node = heappop(heap)
            s.add(node)
            cur = -1*cur

            if node == end_node:
                break
            
            
            if cur < distance[node]:
                continue
            
            for nei, weight in d[node]:
                dist = cur * weight

                if dist > distance[nei] and nei not in s:
                    heappush(heap, (-1*dist, nei))
                    distance[nei] = dist
                    
        # print(distance)
        return distance[end_node] 
