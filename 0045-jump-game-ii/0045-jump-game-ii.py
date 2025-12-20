class Solution:
    def jump(self, nums: List[int]) -> int:
        left, right = 0, 0
        result = 0
        while right<len(nums)-1:
            far = 0
            for i in range(left, right + 1):
                far = max(far, i + nums[i])
            left = right + 1
            right = far
            result += 1

        return result