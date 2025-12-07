class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans,res = [],[]
        def backtrack():
            if len(res)==len(nums):
                ans.append(res[:])
                return ''
            
            for i in range(len(nums)):
                if nums[i] not in res:
                    res.append(nums[i])
                    backtrack()
                    +res.pop()


        backtrack()
        return ans