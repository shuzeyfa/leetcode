class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix=[0]*(len(nums)+1)
        for i in range(len(nums)):
            prefix[i+1]=prefix[i]+nums[i]
        prefix.pop(0)
        minn=min(prefix)
        if minn>=1:
            return 1
        return 1-minn