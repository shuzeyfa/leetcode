class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        ind1 = ind2 = 0

        while ind1 < len(t):
            if ind2 == len(s):
                break
            
            if s[ind2] == t[ind1]:
                ind2 += 1
                ind1 += 1
            else:
                ind1 += 1
        return ind2 == len(s)