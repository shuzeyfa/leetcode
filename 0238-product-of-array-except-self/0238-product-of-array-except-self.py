class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pr=1
        for i in range(len(nums)):
            if nums[i]!=0:
                pr=pr*nums[i]
        res=[]
        if 0 not in nums:
            for i in range(len(nums)):
                temp=pr
                res.append(temp//nums[i])
            return res
        else:
            if nums.count(0)>1:
                return [0]*(len(nums))
            else:
                res=[0]*(len(nums))
                ind=nums.index(0)
                res[ind]=pr
                return res