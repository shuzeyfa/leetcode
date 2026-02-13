class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right= 0, 0
        while right<len(nums):
            while left<len(nums) and nums[left]!=0 :
                left+=1
            while right<left:
                right+=1
            while right<len(nums) and nums[right]==0:
                right+=1
            if right>= len(nums) or left>=len(nums):
                break
            nums[left] ,nums[right]= nums[right],nums[left]
            left+=1
            right+=1
        return (nums)