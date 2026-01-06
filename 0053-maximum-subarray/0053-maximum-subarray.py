class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx=float("-inf")
        current=0
        for i in range(len(nums)):
            current += nums[i]
            if current> maxx:
                maxx=current
            
            if current < 0:
                current=0
        return maxx