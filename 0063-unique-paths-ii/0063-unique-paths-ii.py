class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        
        n = len(obstacleGrid)
        m =  len(obstacleGrid[0])

        @lru_cache(None)
        def dp(i, j):
            if i == n-1 and j == m -1 and obstacleGrid[i][j] != 1:
                return 1
            if i == n or j == m:
                return 0
            
            down = 0
            if i+1 < n and obstacleGrid[i][j] != 1 and obstacleGrid[i+1][j] != 1:
                down += dp(i+1, j)
            right = 0
            if j + 1 < m and obstacleGrid[i][j] != 1 and obstacleGrid[i][j+1] != 1:
                right += dp(i, j+1)
            return down + right
        
        return dp(0, 0)