class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:

        def count(num):
            first = (num // a) + (num // b) + (num // c)
            sec = (num // math.lcm(a,b)) + (num // math.lcm(a, c)) + (num // math.lcm(b, c))
            third = (num // math.lcm(a, b, c))
            return first - sec + third
        

        left, right = min(a, b, c), a*n

        ans = right
        while left <= right:
            mid = (left + right) // 2
            if count(mid) >= n:
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
        