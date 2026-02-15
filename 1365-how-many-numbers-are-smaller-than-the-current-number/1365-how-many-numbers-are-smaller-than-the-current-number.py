class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums2=[]
        for i in nums:
            nums2.append(i)
        nums2.sort()
        l=[]
        for i in range(len(nums)):
            temp=nums2.index(nums[i])
            l.append(temp)
        return l
