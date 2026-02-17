class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k%2==0 or k%5==0:
            return (-1)
        else:
            i=1
            s=0
            while i<=k:
                s=(s*10 +1)%k
                if s==0:
                    return(i)
                i+=1
            return -1
   