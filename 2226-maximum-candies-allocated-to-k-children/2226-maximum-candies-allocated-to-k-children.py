class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        def check(val):
            count = 0
            for i in candies:
                count += (i//val)
            return count>=k
        
        low, high = 1, max(candies)
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans