class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        total = 0
        for i in range(min(n, limit) + 1):
            left = n - i
            if left / limit > 2:
                continue
            m = min(left, limit)
            total += m - (left - m) + 1
        return total
        # for i in range(min(n, limit)):
        #     rem = n - i
        #     val = rem // 2
        #     val2 = val
        #     if rem%2 == 1:
        #         val2 += 1
        #     if val != val2:
        #         total += 2
        #     else:
        #         total += val + 1
        # return total