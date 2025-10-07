class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        def gcd(a,b):
            while b !=0:
                return gcd(b,a%b)
            return a

        for i in range(len(nums)):
            val = nums[i]
            if val == k:
                count += 1
            if val % k != 0:
                continue
            for j in range(i+1,len(nums)):
                val = gcd(val, nums[j])
                if val == k:
                    count += 1
        return count

