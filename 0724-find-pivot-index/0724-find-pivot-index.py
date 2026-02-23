class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        p=[0]*(len(nums)+1)
        for i in range(len(nums)):
            p[i+1]=p[i]+nums[i]
        final=p[len(nums)]
        t=False
        for i in range(1,len(p)):
            if final-p[i]==p[i-1]:
                t=True
                return i-1
        return -1