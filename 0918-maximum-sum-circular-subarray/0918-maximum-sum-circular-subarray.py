class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        right = [0]*len(nums)

        right[-1] = nums[-1]
        summ = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            summ += nums[i]
            right[i] = max(right[i+1], summ)

        maxx = nums[0]
        cur = 0
        for i in nums:
            cur = max(cur + i, i)
            maxx = max(maxx, cur)

        pre = 0
        for i in range(len(nums)-1):
            pre += nums[i]
            maxx = max(maxx, pre+right[i+1])

        return (maxx)