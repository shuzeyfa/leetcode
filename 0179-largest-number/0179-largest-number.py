class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            temp=i
            for j in range(i+1,len(nums)):
                if str(nums[temp])+str(nums[j])<str(nums[j])+str(nums[temp]):
                    temp=j
            if temp!=i:
                nums[temp],nums[i]=nums[i],nums[temp]
        s=""
        for i in nums:
            s+=(str(i))
        to=int(s)
        return str(to)