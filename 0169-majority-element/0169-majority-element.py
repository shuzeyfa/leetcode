class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        d = Counter(nums)

        ans = 0
        count = 0

        for i in d:
            if d[i] > count:
                count = d[i]
                ans = i
        return ans