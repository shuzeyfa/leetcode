class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        d1[0]=1
        ind = nums.index(k)
        bal = 0
        for i in range(ind+1,len(nums)):
            bal += int(nums[i]>k) - int(nums[i]<k)
            d1[bal] += 1

        bal = 0
        for i in range(ind-1,-1,-1):
            bal += int(nums[i]>k) - int(nums[i]<k)
            d2[bal] += 1

        ans = 0
        ans += d1[0]
        ans += d1[1]

        for i in d2:
            ans += d1[-i]*d2[i]
            ans += d1[-i+1]*d2[i]
        return (ans)