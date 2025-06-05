from collections import deque
mat = [[0,0,0],[0,1,0],[1,1,1]]

visited = [[False]*len(mat[0]) for i in range(len(mat))]

ans = [[0]*len(mat[0]) for i in range(len(mat))]
q = deque()
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] == 0:
            visited[i][j] = True
            q.append((i,j,0))
def valid(r,c):
    return 0<=r<len(mat) and 0<=c<len(mat[0]) and visited[r][c] == False

dir = [(0,1),(1,0),(-1,0),(0,-1)]
while q:
    row, col, dis = q.popleft()
    ans[row][col] = dis
    for u,v in dir:
        if valid(row+u,col+v):
            visited[row+u][col+v] = True
            q.append((row+u,col+v,dis+1))
print(ans)


