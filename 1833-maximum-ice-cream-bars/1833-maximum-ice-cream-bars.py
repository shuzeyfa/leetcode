class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        total=0
        l2=[0]*(max(costs)+1)
        for i in costs:
            l2[i]+=1
        l3=[]
        for ind,val in enumerate(l2):
            for j in range(val):
                l3.append(ind)
        for i in range(len(l3)):
            if l3[i]<=coins:
                total+=1
                coins-=(l3[i])
            else:
                break
        return (total)