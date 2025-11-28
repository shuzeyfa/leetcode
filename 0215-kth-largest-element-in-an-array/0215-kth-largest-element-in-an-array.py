class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        l = nlargest(k,nums)
        return l[-1]