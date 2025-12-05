class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (4*self.n)
        self.build(1, 0, self.n - 1, nums)

    def build(self, node, start, end, nums):
        if start == end:
            self.tree[node] = nums[start]
            return
        
        mid = (start + end) // 2
        self.build(2*node, start, mid, nums)
        self.build(2*node + 1, mid + 1, end, nums)
        self.tree[node] = self.tree[2*node] + self.tree[2*node + 1]

        

    def update(self, index: int, val: int) -> None:
        def updateVal(node, start, end, ind, val):
            if start == end:
                self.tree[node] = val
                return

            mid = (start + end) // 2
            if ind <= mid:
                updateVal(2*node, start, mid, ind, val)
            else:
                updateVal(2*node + 1, mid+1, end, ind, val)
            self.tree[node] = self.tree[2*node] + self.tree[2*node + 1]
        return updateVal(1, 0, self.n - 1, index, val)

    def sumRange(self, left: int, right: int) -> int:
        def query(node, start, end, left, right):
            if right < start or left > end:
                return 0
            
            if left <= start and end <= right:
                return self.tree[node]
            
            mid = (start + end) // 2
            return query(2*node, start, mid, left, right) + query(2*node + 1, mid + 1, end, left, right)
        return query(1, 0, self.n - 1, left, right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)