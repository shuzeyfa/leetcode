class Solution:
    def dfs(self,r,c,board,ch):
            m, n = len(board), len(board[0])
            if r < 0 or c < 0 or r >= m or c >= n or board[r][c] == 'X' or ch[r][c]:
                return
            
            ch[r][c] = True

            self.dfs(r - 1, c, board, ch)
            self.dfs(r + 1, c, board, ch)
            self.dfs(r, c - 1, board, ch)
            self.dfs(r, c + 1, board, ch)
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n = len(board), len(board[0])
        ch = [[False]*n for _ in range(m)]
        for i in range(n):
            if board[0][i] == "O":
                self.dfs(0,i,board,ch)

        for i in range(m):
            if board[i][0] == "O":
                self.dfs(i,0,board,ch)
                

        for i in range(n):
            if board[m-1][i] == "O":
                self.dfs(m-1,i,board,ch)
        for i in range(m):
            if board[i][n-1] == "O":
                self.dfs(i,n-1,board,ch)
                

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and not ch[i][j]:
                        board[i][j]="X"
        
        