class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        c=Counter(nums)
        l=[]
        for i in c:
            if c[i]==2:
                l.append(i)
        return l