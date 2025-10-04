class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        @lru_cache(None)
        def dp(ind, total):
            if total == 0:
                return 1

            if ind >= n or total < 0:
                return 0
            
            return dp(ind+1, total) + dp(ind, total - coins[ind])
        
        return dp(0, amount)
