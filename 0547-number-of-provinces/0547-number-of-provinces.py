class Solution:
    def find(self,x):
        while x != self.parent[x]:
            x = self.parent[x]
        return x
    def union(self,x,y):
        rep_x = self.find(x)
        rep_y = self.find(y)
        if rep_x == rep_y:
            return
        if self.rank[rep_x] > self.rank[rep_y]:
            self.parent[rep_y] = rep_x
        elif self.rank[rep_x] < self.rank[rep_y]:
            self.parent[rep_x] = rep_y
        else:
            self.parent[rep_x] = rep_y
            self.rank[rep_y] += 1
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.rank = [0 for i in range(len(isConnected))]
        self.parent = {i:i for i in range(len(isConnected))}
        for i in range(len(isConnected)):
            for j in range(i+1,len(isConnected)):
                if isConnected[i][j] == 1:
                    self.union(i,j) 

        s = set()
        for i in range(len(isConnected)):
            val = self.find(i)
            s.add(val)
        return len(s)
        
