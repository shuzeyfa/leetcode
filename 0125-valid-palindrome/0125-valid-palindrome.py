class Solution:
    def isPalindrome(self, s: str) -> bool:
        new=''.join(char for char in s if char.isalnum())
        new=new.lower()
        if new==new[::-1]:
            return True
        else:
            return False
        