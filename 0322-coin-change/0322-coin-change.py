class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        s = sum(coins)

        if amount == 0:
            return 0

        memo = {}
        def dp(ind, total):

            if total == 0:
                return 0
            
            if total < 0 or ind >= len(coins):
                return float("inf")

            if (ind, total) not in memo:
                take = dp(ind, total - coins[ind]) + 1
                leave = dp(ind + 1, total)
                memo[(ind, total)] = min(take, leave)

            return memo[(ind, total)]
        
        ans = dp(0, amount) 
        return ans if ans != float("inf") else -1