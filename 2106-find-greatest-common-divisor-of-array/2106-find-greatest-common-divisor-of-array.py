class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minn, maxx = min(nums), max(nums)
        def gcd(a,b):
            while b != 0:
                return gcd(b,a%b)
            return a
        return gcd(maxx,minn)