class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix=[0] * (len(nums)+1)
        for i in range(len(nums)):
            prefix[i+1]=prefix[i]+nums[i]
        dq=deque()
        mi=float('inf')
        for i in range(len(nums)+1):
            while dq and prefix[i] - prefix[dq[0]] >= k:
                mi = min(mi, i - dq.popleft())
            while dq and prefix[i] <= prefix[dq[-1]]:
                dq.pop()
            dq.append(i)
        return mi if  mi != float('inf') else -1 