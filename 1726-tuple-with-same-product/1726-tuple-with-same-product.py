class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        d=defaultdict(int)

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                prod=nums[i]*nums[j]
                d[prod]+=1
        final=sum((count*(count-1))//2 for count in d.values() if count>1)
        return final*8