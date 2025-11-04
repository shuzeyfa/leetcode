class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)

        def backtrack(idx, path):
            if idx >= n:
                return reduce(lambda a,b: a ^ b, path)
            #not take
            xor = backtrack(idx + 1, path)
            #take
            path.append(nums[idx])
            xor += backtrack(idx + 1, path)
            path.pop()
            return xor
        return backtrack(0, [0])