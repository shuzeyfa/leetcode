class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        visited = [[False]*len(mat[0]) for i in range(len(mat))]
        ans = [[0]*len(mat[0]) for i in range(len(mat))]

        q = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append((i,j,0))
                    visited[i][j] = True
        def valid(r,c):
            return 0<=r<len(mat) and 0<=c<len(mat[0]) and visited[r][c] == False
        dir = [(0,1),(1,0),(-1,0),(0,-1)]
        while q:
            row, col, dis = q.popleft()
            ans[row][col] = dis
            for i,j in dir:
                if valid(row+i, col+j):
                    visited[row+i][col+j] = True
                    q.append((row+i, col+j, dis+1))
        return ans 