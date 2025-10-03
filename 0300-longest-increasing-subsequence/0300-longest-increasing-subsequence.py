class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        
        memo = [[-1]*(n+1) for i in range(n+1)]

        def dp(ind, last):
            if ind == n:
                return 0
            
            if memo[ind][last] != -1:
                return memo[ind][last]
            
            include = 0
            if last == n or nums[ind] > nums[last]:
                include = dp(ind+1, ind) + 1
            exclude = dp(ind+1, last)
            memo[ind][last] = max(include, exclude)
            return memo[ind][last]
            

        return dp(0, n)