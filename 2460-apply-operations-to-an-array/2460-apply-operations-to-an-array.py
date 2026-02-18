class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if i!=len(nums)-1:
                if nums[i]==nums[i+1]:
                    nums[i],nums[i+1]=nums[i]*2,0
        l2=[x for x in nums if x!=0]
        l2=l2+[0]*(len(nums)-len(l2))
        return l2