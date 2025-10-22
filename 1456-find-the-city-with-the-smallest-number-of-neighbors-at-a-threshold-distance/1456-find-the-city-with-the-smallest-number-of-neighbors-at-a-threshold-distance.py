class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        d = defaultdict(set)

        for a, b, w in edges:
            d[a].add((b, w))
            d[b].add((a, w))
        
        val = n - 1
        ans = 0
        # print(d)
        def find(num):
            s = set()
            s.add(num)

            heap = [(0, num)]
            while heap:
                cur, node = heappop(heap)
                s.add(node)
                


                for nei, weight in d[node]:
                    dist = weight + cur
                    if dist <= distanceThreshold and nei not in s:
                        heappush(heap, (dist, nei))
                        
          
            return len(s) - 1



        for i in range(n):
            val2 = find(i)
            # print(val2)
            if val2 < val:
                val = val2
                ans = i
            elif val2 == val:
                ans = i
        return ans