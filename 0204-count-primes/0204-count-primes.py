class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1 or n == 2:
            return 0
        

        def erato(n):

            is_prime = [True]*n
            is_prime[0] = False
            is_prime[1] = False

            d = 2
            while d*d <= n:
                if is_prime[d]:
                    temp = d*d
                    for i in range(temp, n, d):
                        is_prime[i] = False
                d += 1
            return is_prime

        
        l = erato(n)
        ans = 0
        for i in range(n):
            if l[i]:
                ans += 1
        return ans