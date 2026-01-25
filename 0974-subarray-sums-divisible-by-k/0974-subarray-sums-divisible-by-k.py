class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        val=0
        tot=0
        d=Counter()
        d[0]=1
        for n in nums:
            tot += n
            rem = tot % k
            val += d.get(rem,0)
            d[rem] += 1
        return val