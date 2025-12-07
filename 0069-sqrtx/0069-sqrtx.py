class Solution:
    def mySqrt(self, x: int) -> int:
        ans = float("inf")
        if x<2:
            return x
        low = 2
        high = x//2
        while low<= high:
            mid = (low+high)//2
            if mid*mid == x:
                return mid
            elif mid * mid>x:
                high = mid - 1
            else:
                low = mid + 1
        return high
