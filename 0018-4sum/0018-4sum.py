class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        l2=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            else:
                for j in range(i+1,len(nums)):
                    left,right=j+1,len(nums)-1
                    while left<right:
                        summ=nums[i]+nums[j]+nums[left]+nums[right]
                        if summ==target:
                            if [nums[i],nums[j],nums[left],nums[right]] not in l2:
                                l2.append([nums[i],nums[j],nums[left],nums[right]])
                            while left<right and nums[left]==nums[left+1]:
                                left+=1
                            while left<right and nums[right]==nums[right-1]:
                                right-=1
                            left+=1
                            right-=1
                        elif summ>target:
                            right-=1
                        else:
                            left+=1
        return l2
                                