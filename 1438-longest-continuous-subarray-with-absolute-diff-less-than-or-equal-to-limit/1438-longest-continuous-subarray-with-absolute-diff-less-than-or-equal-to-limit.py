class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        inc = deque()
        dec = deque()

        left = 0
        count = 0
        for i in range(len(nums)):
            while dec and dec[-1] < nums[i]:
                dec.pop()
            dec.append(nums[i])

            while inc and inc[-1] > nums[i]:
                inc.pop()
            inc.append(nums[i])

            while dec[0] - inc[0] > limit:
                if dec[0] == nums[left]:
                    dec.popleft()

                if inc[0] == nums[left]:
                    inc.popleft()
                
                left += 1

            count = max(count,i - left + 1)
        return count
