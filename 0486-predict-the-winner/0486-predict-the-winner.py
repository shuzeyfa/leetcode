class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def find(left,right):
            if left == right:
                return nums[right]

            return max(nums[left] - find(left+1,right), nums[right] - find(left,right-1))

        return find(0,len(nums)-1) >= 0