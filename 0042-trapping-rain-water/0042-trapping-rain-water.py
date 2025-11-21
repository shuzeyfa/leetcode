class Solution:
    def trap(self, height: List[int]) -> int:
        
        stack = []
        ans = 0

        for i in range(len(height)):

            while stack and height[i] > height[stack[-1]]:

                last = stack.pop()

                if not stack:
                    break
                
                distance = i - stack[-1] - 1

                minHeight = min(height[i], height[stack[-1]]) - height[last]

                ans += (distance * minHeight)
            stack.append(i)

            
        return ans