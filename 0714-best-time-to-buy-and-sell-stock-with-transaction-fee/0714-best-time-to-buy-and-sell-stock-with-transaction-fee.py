class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        memo = {}
        def dp(ind, odd):
            if ind == len(prices):
                return 0
            
            if (ind, odd) not in memo:
                if not odd:
                    include = dp(ind+1, not odd) - prices[ind]
                    exclude = dp(ind+1, odd)
                    memo[(ind, odd)] = max(include, exclude )
                else:
                    include = dp(ind+1, not odd) + prices[ind] - fee
                    exclude = dp(ind+1, odd) 
                    memo[(ind, odd)] = max(include, exclude)
            
            return memo[(ind, odd)]
        
        return dp(0, False)