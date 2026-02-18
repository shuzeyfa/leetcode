class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        index=len(s)-1
        for i in range(len(s)//2):
            s[i],s[index]=s[index],s[i]
            index-=1
        return s