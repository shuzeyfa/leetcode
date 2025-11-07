class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        left, right = 0, 0

        while right < len(nums):

            nums[left] = nums[right]
            right += 1
            if right < len(nums) and nums[right] == nums[left]:
                left += 1
                nums[left] = nums[right]
                right += 1
            
            while right < len(nums) and nums[right] == nums[left]:
                right += 1
            left += 1
        return left