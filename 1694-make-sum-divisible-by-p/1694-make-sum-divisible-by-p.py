class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        prefix = 0
        seen = {0: -1}
        ans = len(nums)

        rem = sum(nums) % p

        if rem == 0:
            return 0

        for i in range(len(nums)):
            prefix = (prefix + nums[i]) % p
            target = (prefix - rem) % p
            if target in seen:
                ans = min(ans, i - seen[target])
            seen[prefix] = i
        return ans if ans < len(nums) else -1