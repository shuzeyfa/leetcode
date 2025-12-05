class SegmentTree:
    def __init__(self, n, arr):
        self.n = n
        self.tree = [0] * (4 * n)
        self.build(1, 0, n-1, arr)
    
    def build(self, node, start, end, arr):
        if start == end:
            self.tree[node] = arr[start]
            return
        mid = (start + end) // 2
        self.build(2*node, start, mid, arr)
        self.build(2*node+1, mid+1, end, arr)
        self.tree[node] = self.tree[2*node] + self.tree[2*node+1]
    
    # Change arr[idx] = val
    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        if idx <= mid:
            self.update(2*node, start, mid, idx, val)
        else:
            self.update(2*node+1, mid+1, end, idx, val)
        self.tree[node] = self.tree[2*node] + self.tree[2*node+1]
    
    # Sum from l to r (0-based indices)
    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        return self.query(2*node, start, mid, l, r) + self.query(2*node+1, mid+1, end, l, r)

class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        n = len(nums)

        peak = [0]*n

        def checkPeak(ind):
            if ind<= 0 or ind >= n-1:
                return 0
            return 1 if (nums[ind] > nums[ind-1] and nums[ind] > nums[ind+1]) else 0

        for i in range(1, n-1):
            peak[i] = checkPeak(i)
        
        
        seg = SegmentTree(n, peak)
        
        ans = []

        for i in range(len(queries)):

            typ = queries[i][0]

            if typ == 1:

                left, right = queries[i][1], queries[i][2]

                if right - left < 2:
                    ans.append(0)
                    continue

                val = seg.query(1, 0, n-1, left+1, right-1)
                ans.append(val)
                

            else:
                ind, val = queries[i][1], queries[i][2]

                nums[ind] = val

                for ind2 in range(ind-1, ind+2):
                    if 0 <= ind2 < n:
                        ch = checkPeak(ind2)
                        seg.update(1, 0, n-1, ind2, ch)

        return ans











        