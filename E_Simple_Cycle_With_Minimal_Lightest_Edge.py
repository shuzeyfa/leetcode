from collections import defaultdict, deque

class UnionFind:
    def __init__(self, t):
        self.parent = [i for i in range(t)]
        self.rank = [0 for _ in range(t)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        p_x = self.find(x)
        p_y = self.find(y)
        if p_x != p_y:
            if self.rank[p_x] > self.rank[p_y]:
                self.parent[p_y] = p_x
            elif self.rank[p_x] < self.rank[p_y]:
                self.parent[p_x] = p_y
            else:
                self.parent[p_x] = p_y
                self.rank[p_y] += 1
            return True
        return False

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    edge = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        edge.append((w, u, v))
    
    edge.sort(reverse=True)

    graph = defaultdict(list)
    last = (-1, -1)
    ans = float("inf")

    uf = UnionFind(n)
    for w, u, v in edge:
        if not uf.union(u, v):
            last = (u, v)
            ans = w
        else:
            graph[u].append(v)
            graph[v].append(u)

    # Use BFS to find path from last[0] to last[1]
    parent_map = {}
    visited = set()
    q = deque()
    q.append(last[0])
    visited.add(last[0])

    while q:
        node = q.popleft()
        if node == last[1]:
            break
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent_map[neighbor] = node
                q.append(neighbor)

    
    path = []
    current = last[1]
    while current != last[0]:
        path.append(current)
        current = parent_map[current]
    path.append(last[0])
    path.reverse()


    print(ans, len(path))
    print(' '.join(str(x + 1) for x in path))
