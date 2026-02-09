class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxx=0
        left, right= 0,0
        while right<len(nums):
            if nums[right]==1:
                right+=1
                maxx=max(maxx,right-left)
            else:
                if k==0:
                    maxx=max(maxx,right-left)
                    while left<right and nums[left]!=0:
                        left+=1
                    left+=1
                    right+=1
                else:
                    right+=1
                    maxx=max(maxx,right-left)
                    k-=1
        return maxx