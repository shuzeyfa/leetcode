class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minn = float("inf")
        ans = 0
        for i in prices:
            minn = min(minn, i)

            if i - minn > 0:
                ans = max(ans, i - minn)
        return ans