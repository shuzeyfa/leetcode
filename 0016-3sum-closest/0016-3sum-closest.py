class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        maxx=float('inf')
        check=float('inf')
        for i in range(len(nums)):
            left,right=i+1,len(nums)-1
            while left<right:
                temp=nums[i]+nums[left]+nums[right]
                if check>abs(target-temp):
                    maxx=temp
                    check=abs(target-temp)
                if temp>target:
                    right-=1
                else:
                    left+=1
        return maxx