class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p1=Counter(p)
        d=Counter(s[:len(p)])
        index=0
        l=[]
        if d==p1:
            l.append(0)
        for i in range(len(p),len(s)):
            d[s[i]]+=1
            d[s[index]]-=1
            if d[s[index]]==0:
                d.pop(s[index])
            index+=1
            if d==p1:
                l.append(index)
        return (l)