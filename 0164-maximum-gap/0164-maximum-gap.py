class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)<2:
            return 0
        maxx=0
        for i in range(len(nums)-1):
            maxx=max(maxx,abs(nums[i]-nums[i+1]))
        return maxx