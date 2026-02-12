class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ=sum(nums[:k])
        index1=k
        index2=0
        maxx=summ/k
        while index1<len(nums):
            summ-=(nums[index2])
            summ+=(nums[index1])
            maxx=max(maxx,summ/k)
            index1+=1
            index2+=1
        return (maxx)