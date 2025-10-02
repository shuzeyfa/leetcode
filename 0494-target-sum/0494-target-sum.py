class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        ans = 0
        memo = {}
        def dp(ind, total):
            if ind == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            
            if (ind, total) not in memo:
                add = dp(ind+1, total + nums[ind])
                minus = dp(ind+1, total - nums[ind])
                memo[(ind, total)] = add + minus
            
            return memo[(ind, total)]

        return dp(0, 0)