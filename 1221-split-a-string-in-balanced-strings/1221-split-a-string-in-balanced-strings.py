class Solution:
    def balancedStringSplit(self, s: str) -> int:
        right = left = 0
        count = 0
        for i in s:
            if i == "R":
                right += 1
            else:
                left += 1
            if left == right:
                count += 1
                left, right = 0,0
        return count