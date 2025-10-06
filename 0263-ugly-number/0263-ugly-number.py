class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        
        def prime(n):
            fact = set()

            d = 2
            while d*d <= n:
                while n%d == 0:
                    fact.add(d)
                    n //= d
                d += 1
            if n > 1:
                fact.add(n)
            # print(fact)
            if len(fact) > 3:
                return False
            
            if 2 in fact:
                fact.remove(2)
            if 3 in fact:
                fact.remove(3)
            if 5 in fact:
                fact.remove(5)
            if len(fact) > 0:
                return False
            return True
        return prime(n)