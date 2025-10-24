class Solution:
    def isPalindrome(self, x: int) -> bool:
        x2=str(x)
        x3=x2[::-1]
        if x2==x3:
            return True
        else:
            return False