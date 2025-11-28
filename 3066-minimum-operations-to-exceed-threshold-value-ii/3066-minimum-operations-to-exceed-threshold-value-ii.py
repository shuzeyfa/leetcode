class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        minn = heappop(nums)
        count = 0
        while len(nums) >= 1 and minn < k:
            sec = heappop(nums)
            val = minn*2 + sec
            heappush(nums,val)
            minn = heappop(nums)
            count += 1
        return count