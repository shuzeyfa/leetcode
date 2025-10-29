class Solution:
    def numTrees(self, n: int) -> int:

        @lru_cache(None)
        def dp(n):
            
            if n <= 1:
                return 1
            
            total = 0

            for i in range(1, n+1):
                left = dp(i-1)
                right = dp(n - i)
                total += left*right
            return total
        
        
        return dp(n)