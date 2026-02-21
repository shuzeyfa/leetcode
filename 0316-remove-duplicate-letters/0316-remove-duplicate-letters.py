class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        i=0
        while i<len(s):
            if i>0:
                temp=s[i]
                if temp in s[:i]:
                    s=s[:i]+s[i+1:]
                    i-=1
                else:
                    t=False
                    j=i-1
                    while j>-1:
                        if s[j]>temp:
                            if s[j] in s[i+1:] and t==False:
                                s=s[:j]+s[j+1:]
                                i-=1
                            else:
                                t=True
                        j-=1
            i+=1
        return s