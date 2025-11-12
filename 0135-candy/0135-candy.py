class Solution:
    def candy(self, ratings: List[int]) -> int:

        n = len(ratings)
        
        ans = [1]*n

        d = defaultdict(list)

        for i in range(n):
            d[ratings[i]].append(i)
        
        l = ratings[:]
        
        ratings.sort()

        for i in range(n):
            val = d[ratings[i]].pop()

            if val - 1 > -1 and l[val-1] > l[val]:
                ans[val-1] = max(ans[val-1], ans[val] + 1)
            
            if val + 1 < n and l[val+1] > l[val]:
                ans[val+1] = max(ans[val+1], ans[val] + 1)

        # print(ans)
        return sum(ans)