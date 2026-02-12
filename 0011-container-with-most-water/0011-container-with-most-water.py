class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) -1
        maxx=0
        while left<right:
            length= min(height[left],height[right])
            width= right - left
            maxx = max(maxx, length*width)
            if height[left]<=height[right]:
                left+=1
            else:
                right-=1
        return maxx