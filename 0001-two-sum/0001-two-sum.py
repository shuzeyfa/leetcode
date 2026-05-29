class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = defaultdict(list)

        for i in range(len(nums)):

            d[nums[i]].append(i)
        

        for i in nums:

            rem = target - i

            if rem in d and rem != i:
                return sorted([d[rem].pop(), d[i].pop()])
            
            if rem == i:
                if len(d[rem]) > 1:
                    return sorted([d[rem].pop(), d[rem].pop()])