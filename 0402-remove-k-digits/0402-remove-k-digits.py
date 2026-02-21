class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        s=[]
        for i in range(len(num)):
            while k>0 and s and s[-1] >num[i]:
                s.pop()
                k-=1
            s.append(num[i])
        while k>0 and s:
            s.pop()
            k-=1
        f="".join(s)
        f=f.lstrip("0")
        return f if len(f)>0 else "0"