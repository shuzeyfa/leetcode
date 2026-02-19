class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        rep=floor(len(nums)/3)
        c=Counter(nums)
        l2=[]
        for i in c:
            if c[i]>rep:
                l2.append(i)
        return l2