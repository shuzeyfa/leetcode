class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        n , m = len(dungeon), len(dungeon[0])

        @lru_cache(None)
        def dp(i, j):

            if i == n - 1 and j == m - 1:
                return max(1, 1 - dungeon[i][j])
            
            if i == n or j == m:
                return float("inf")
            
            return max(1, -dungeon[i][j] + min(dp(i+1, j), dp(i, j+1)) )
            
        
        return dp(0, 0)