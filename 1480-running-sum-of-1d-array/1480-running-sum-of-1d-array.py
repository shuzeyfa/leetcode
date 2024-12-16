class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        p=[0]*(len(nums)+1)
        for i in range(len(nums)):
            p[i+1]=p[i]+nums[i]
        p.pop(0)
        return p