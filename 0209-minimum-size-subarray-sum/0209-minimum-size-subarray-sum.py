class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right =0 ,0
        summ, tot=0 ,float("inf")
        while right<len(nums):
            summ+=(nums[right])
            if summ>=target:
                tot=min(tot,(right-left)+1)
                while summ>target:
                    summ-=(nums[left])
                    left+=1
                    if summ>=target:
                        tot=min(tot,(right-left)+1)
                right+=1
            else:
                right+=1

        if tot==float("inf"):
            return (0)
        return (tot)