class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        def valid(r,c):
            return 0<=r<len(grid) and 0<=c<len(grid[0])
        
        visit = [[False]*len(grid[0]) for i in range(len(grid))]

        opp = {"up":"down", "down":"up", "left":"right", "right":"left"}

        poss = {
            1:set(["right","left"]),
            2:set(["up","down"]),
            3:set(["left","down"]),
            4:set(["down","right"]),
            5:set(["up","left"]),
            6:set(["up","right"])
        }
        q = deque([(0,0)])
        while q:
            row, col = q.popleft()
            if row  == len(grid)-1 and col  == len(grid[0])-1:
                return True

            visit[row][col] = True
            val = grid[row][col]

            for i in poss[val]:
                if i == "right":
                    row2,col2 = row, col + 1
                    if valid(row2, col2) and visit[row2][col2] == False and "left" in poss[grid[row2][col2]]:
                        q.append((row2,col2))
                elif i == "left":
                    row2, col2 = row, col - 1
                    if valid(row2, col2) and visit[row2][col2] == False and  "right" in poss[grid[row2][col2]]:
                        q.append((row2,col2))
                elif i == "up":
                    row2, col2 = row - 1, col
                    if valid(row2, col2) and visit[row2][col2] == False and "down" in poss[grid[row2][col2]]:
                        q.append((row2,col2))
                else:
                    row2, col2 = row +1, col
                    if valid(row2, col2) and visit[row2][col2] == False and "up" in poss[grid[row2][col2]]:
                        q.append((row2,col2))
        return False

