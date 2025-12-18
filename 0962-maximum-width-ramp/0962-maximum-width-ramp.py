class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n=len(nums)
        indexed=[(num,i)for i, num in enumerate(nums)]
        indexed.sort()
        ma=0
        mi=float('inf')
        for value,index in indexed:
            mi=min(mi,index)
            ma=max(ma,index-mi)
        return ma            