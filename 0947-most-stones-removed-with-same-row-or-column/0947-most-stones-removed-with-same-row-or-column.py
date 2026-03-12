
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {i:i for i in range(len(stones))}
        rank = [0]*len(stones)

        def find(x):
            if x == parent[x]:
                return x
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x,y):
            rep_x = find(x)
            rep_y = find(y)
            if rep_x != rep_y:
                if rank[rep_x] > rank[rep_y]:
                    parent[rep_y] = rep_x
                elif rank[rep_x] < rank[rep_y]:
                    parent[rep_x] = rep_y
                else:
                    parent[rep_y] = rep_x
                    rank[rep_x] += 1

        for i in range(len(stones)):
            for j in range(len(stones)):
                if i!=j and (stones[j][0] == stones[i][0] or stones[j][1]==stones[i][1]):
                    union(i,j)
        s = set()
        for i in range(len(stones)):
            rep = find(i)
            s.add(rep)
        return len(stones) - len(s)

        