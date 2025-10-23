class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        d = defaultdict(list)
        for u, v, w in flights:
            d[u].append((v, w))
        
        # Min-heap: (cost, city, stops)
        heap = [(0, src, 0)]
        # Track minimum stops to reach each city
        min_stops = [float('inf')] * n
        
        while heap:
            cost, city, stops = heapq.heappop(heap)
            
            if city == dst:
                return cost
            
            if stops > k:
                continue
                
            # If we've reached this city with fewer stops, skip
            if stops >= min_stops[city]:
                continue
            min_stops[city] = stops
            
            for neighbor, price in d[city]:
                heapq.heappush(heap, (cost + price, neighbor, stops + 1))
        
        return -1