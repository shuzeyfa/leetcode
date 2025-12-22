class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row = []
        for i in range(len(grid)):
            row.append(max(grid[i]))
        col = []
        for j in range(len(grid)):
            max_=0
            for grids in grid:
                max_=max(grids[j],max_)
            col.append(max_)
        tot = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                tot += abs(grid[i][j]-min(row[i],col[j]))

        return tot

        