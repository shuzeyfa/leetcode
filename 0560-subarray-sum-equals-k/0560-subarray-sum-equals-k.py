class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d=Counter()
        d[0]=1
        count=0
        presum=0
        for i in range(len(nums)):
            presum+=(nums[i])
            rem=presum-k
            count+=(d[rem])
            d[presum]+=1
        return count