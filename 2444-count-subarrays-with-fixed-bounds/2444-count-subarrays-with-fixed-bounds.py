class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        left,right,wrong = -1,-1,-1

        for i, num in enumerate(nums):
            if num >maxK or num < minK:
                wrong = i

            if num == minK:
                left = i

            if num == maxK:
                right = i

            count += (max(0, min(right,left) - wrong))
        return count