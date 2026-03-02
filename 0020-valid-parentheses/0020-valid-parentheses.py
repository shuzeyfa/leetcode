class Solution:
    def isValid(self, s: str) -> bool:
        t=True
        l=[]
        for i in range(len(s)):
            if s[i]=="(" or s[i]=="{" or s[i]=="[":
                l.append(s[i])
            elif s[i]==")":
                if len(l)!=0:
                    if l[len(l)-1]=="(":
                        l.pop(-1)
                    else:
                        t=False
                        break
                else:
                    t=False
                    break
            elif s[i]=="]":
                if len(l)!=0:
                    if l[len(l)-1]=="[":
                        l.pop(-1)
                    else:
                        t=False
                        break
                else:
                    t=False
                    break
            elif s[i]=="}":
                if len(l)!=0:
                    if l[len(l)-1]=="{":
                        l.pop(-1)
                    else:
                        t=False
                        break
                else:
                    t=False
                    break
        if len(l)!=0:
            t=False
        if t==True:
            return True
        else:
            return False