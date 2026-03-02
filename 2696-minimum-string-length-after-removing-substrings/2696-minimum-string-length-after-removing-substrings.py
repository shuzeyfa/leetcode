class Solution:
    def minLength(self, s: str) -> int:
        while "AB"  in s  or "CD" in s:
            if "AB" in s:
                index=s.index("AB")
                if index==0:
                    temp=s[2:]
                    s=temp
                else:
                    temp1=s[0:index]
                    temp2=s[index+2:]
                    s=temp1+temp2
            elif "CD" in s:
                index=s.index("CD")
                if index==0:
                    temp=s[2:]
                    s=temp
                else:
                    temp1=s[0:index]
                    temp2=s[index+2:]
                    s=temp1+temp2
        return len(s)           