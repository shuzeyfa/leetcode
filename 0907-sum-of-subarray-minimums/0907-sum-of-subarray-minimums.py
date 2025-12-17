class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        res = 0
        for i, num in enumerate(arr):
            while stack and stack[-1][1] > num:
                j, n = stack.pop()
                left = j - stack[-1][0] if stack else j + 1
                right = i - j 
                res += (n * left * right)
            stack.append((i,num))

        for i in range(len(stack)):
            j, n = stack[i]
            left = j - stack[i-1][0] if i>0 else j + 1
            right = len(arr) - j
            res += (n * right * left)
        return res % (10**9 + 7)
        