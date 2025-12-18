class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        minn = nums[0]
        stack = []

        for n in nums[1:]:
            while stack and n >= stack[-1][0]:
                stack.pop()
            
            if stack and n > stack[-1][1]:
                return True

            stack.append([n,minn])
            minn = min(minn, n)

        return False