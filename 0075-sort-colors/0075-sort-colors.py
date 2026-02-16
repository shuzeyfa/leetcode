class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            temp=i
            for j in range(i,len(nums)):
                if nums[j]<nums[temp]:
                    temp=j
            if temp!=i:
                nums[temp],nums[i]=nums[i],nums[temp]
        return (nums)