class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        l2=[0]*len(nums)
        for i in requests:
            l2[i[0]]+=1
            if i[1]+1<len(nums):
                l2[i[1]+1]-=1
        pre=[0]*len(nums)
        pre[0]=l2[0]
        for i in range(1,len(nums)):
            pre[i]=pre[i-1]+l2[i]
        nums.sort()
        tot=0
        pre.sort(reverse=True)
        for i in pre:
            tot += (nums[-1]*i)
            nums.pop()

        return (tot % ((10**9)+7))