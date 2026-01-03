class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        tot=0
        d=Counter()
        d[0]=1
        summ=0
        for i in nums:
            summ+=i
            dif=summ-goal
            tot+=(d.get(dif,0))
            d[summ]+=1
        return tot