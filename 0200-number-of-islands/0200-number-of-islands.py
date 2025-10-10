class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dir = [(0,1),(1,0),(-1,0),(0,-1)]

        def valid(row2,col2):
            return 0<=row2<len(grid) and 0<=col2<len(grid[0])

        def dfs(i,j):
            grid[i][j] = "0"
            for row,col in dir:
                new_row = row+i
                new_col = col + j
                if valid(new_row,new_col) and grid[new_row][new_col] == "1":
                    dfs(new_row,new_col)

            return


        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i,j)

        return ans
