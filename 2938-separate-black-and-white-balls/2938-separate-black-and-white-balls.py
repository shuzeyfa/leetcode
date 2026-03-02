class Solution:
    def minimumSteps(self, s: str) -> int:
        count=0
        t=0
        for  i in range(len(s)):
            if s[i]=="1":
                t+=1
            else:
                count+=t
        return count                  
            