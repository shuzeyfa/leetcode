class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n == 1:
            return 5
        
        primes = pow(4, (n // 2), 10**9 + 7) 

        even = n // 2
        even += (n%2)

        val = pow(5,even, 10**9 + 7) 
        return (val * primes) % (10**9+7)