class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n==1:
            return 2
        elif n%2==1:
            return 2*n
        else:
            return n