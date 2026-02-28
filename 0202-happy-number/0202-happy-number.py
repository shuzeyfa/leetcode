class Solution:
    def isHappy(self, n: int) -> bool:
        c=[]
        while n!=1 and n not in c:
            c.append(n)
            n=sum(int(digit)**2 for digit in str(n))
        return n==1    
            