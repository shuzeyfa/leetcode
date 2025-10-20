class Solution:
    def frequencySort(self, s: str) -> str:
        c=Counter(s)
        d=dict(sorted(c.items(),key=lambda item:item[1],reverse=True))
        s2=""
        for i in d:
            s2+=(i*(d[i]))
        return s2