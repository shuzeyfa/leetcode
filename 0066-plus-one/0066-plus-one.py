class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        for i in digits:
            s+=str(i)  
        index=int(s)+1
        s2=str(index)
        l=[]
        for j in range(len(s2)):
            l.append(int(s2[j]))
        return l    