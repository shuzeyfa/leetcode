class NumArray:

    def __init__(self, nums: List[int]):
        self.p=[0]*(len(nums))
        self.p[0]=nums[0]
        for i in range(1,len(nums)):
            self.p[i]=self.p[i-1]+nums[i]
        


    def sumRange(self, left: int, right: int) -> int:
        temp=self.p[right]
        if left==0:
            temp2=0
        else:
            temp2=self.p[left-1]
        return temp-temp2


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)