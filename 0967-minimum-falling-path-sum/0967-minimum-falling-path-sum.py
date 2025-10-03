class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        n, m = len(matrix), len(matrix[0])
        # memo = [[-1]*(m) for i in range(n)]
        memo = {}
        
        def dp(i, j):
            if i == n:
                return 0
            
            if j < 0 or j == m:
                return float("inf")
            
            if (i, j) not in memo:
                memo[(i, j)] = min(dp(i+1, j-1) + matrix[i][j], dp(i+1, j) + matrix[i][j], dp(i+1, j+1) + matrix[i][j])
            return memo[(i, j)]
        
        ans = float("inf")
        for k in range(len(matrix[0])):
            ans = min(ans, dp(0, k))
        return ans