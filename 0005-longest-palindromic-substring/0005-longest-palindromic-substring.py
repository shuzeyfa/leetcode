class Solution:
    def longestPalindrome(self, s: str) -> str:
        left=0
        final=""
        while left<len(s):
            right=len(s)
            t=False
            while right>left:
                s1=s[left:right]
                if s1==s1[::-1]:
                    temp=s1
                    t=True
                    break
                right-=1
            left+=1
            if t==True:
                if len(temp)>len(final):
                    final=temp
        return final