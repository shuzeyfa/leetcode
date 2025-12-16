class Solution:
    def trailingZeroes(self, n: int) -> int:
        def fact(n):
            if n == 0 or n == 1:
                return 1

            return n*fact(n-1)

        string = fact(n)
        if string == 0:
            return 0
        count = 0
        while string > 0:
            k = string % 10
            string = string // 10
            if k == 0:
                count += 1
            else:
                break
        return count
        