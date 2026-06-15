class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        ans = []

        val = []

        for start, end in intervals:
            val.append((start, -1))
            val.append((end, 1))
        
        val.sort()
        # print(val)

        count = 0

        first = float("inf")

        for start, end in val:
            if end == -1:
                if count == 0:
                    first = start
                count += 1
            else:
                if count == 1:
                    ans.append([first, start])
                    first = float('inf')
                count -= 1
        return ans