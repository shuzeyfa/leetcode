class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        temp=Counter(nums)
        output=[i for i in temp.keys() if temp[i]>1]
        return output[0]