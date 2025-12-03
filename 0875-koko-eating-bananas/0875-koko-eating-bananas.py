class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(n):
            # nonlocal ans
            count = 0
            for i in piles:
                count += (math.ceil(i/n))
            
            return count<=h
        low = 1
        high = sum(piles)
        ans = float("inf")
        while low<=high:
            mid = (low + high) //2
            if check(mid):
                ans = min(mid,ans)
                high = mid - 1
            else:
                low = mid + 1
        return ans