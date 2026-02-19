class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        l2=[]
        summ=sum(x for x in nums if x%2==0)
        for i in queries:
            temp=nums[i[1]]
            nums[i[1]]+=i[0]
            if temp%2==0:
                summ-=temp
            if (temp+i[0])%2==0:
                summ+=(temp+i[0])
                l2.append(summ)
            else:
                l2.append(summ)
        return (l2)