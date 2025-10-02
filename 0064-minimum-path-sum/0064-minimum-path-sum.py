class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        n, m = len(grid), len(grid[0])
        memo = {}

        def dp(i, j):
            if i == n - 1 and j == m - 1:
                return grid[i][j]
            if i == n or j == m:
                return float("inf")
            
            if (i, j) not in memo:
                memo[(i, j)] = min(dp(i+1, j) + grid[i][j], dp(i, j+1) + grid[i][j])
            
            return memo[(i, j)]
        
        return dp(0, 0)

            