class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        p=[0]*(len(nums))
        p[0]=nums[0]
        for i in range(1,len(nums)):
            p[i]=p[i-1]+nums[i]
        return p