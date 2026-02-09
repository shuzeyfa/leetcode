class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        p1=Counter(s1)
        p2=Counter(s2[:len(s1)])
        index=0
        if p1==p2:
            return True
        for i in range(len(s1),len(s2)):
            p2[s2[i]]+=1
            p2[s2[index]]-=1
            if p2[s2[index]]==0:
                p2.pop(s2[index])
            if p2==p1:
                return True
            index+=1
        return False