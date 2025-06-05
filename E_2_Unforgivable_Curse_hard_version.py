class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx != fy:
            self.parent[fy] = fx  # Union

def can_transform(s, t, k):
    n = len(s)
    if len(s) != len(t):
        return False

    uf = UnionFind(n)

    # Step 1: Connect indices that can be swapped
    for i in range(n):
        if i + k < n:
            uf.union(i, i + k)
        if i + k + 1 < n:
            uf.union(i, i + k + 1)

    # Step 2: Group indices by their root parent
    from collections import defaultdict, Counter

    groups = defaultdict(list)
    for i in range(n):
        root = uf.find(i)
        groups[root].append(i)

    # Step 3: Check if s and t can be made equal in each group
    for group_indices in groups.values():
        s_chars = [s[i] for i in group_indices]
        t_chars = [t[i] for i in group_indices]

        if Counter(s_chars) != Counter(t_chars):
            return False

    return True
for _ in range(int(input())):
    n, k = map(int,input().split())
    s = input()
    t = input()

    if can_transform(s, t, k):
        print("YES")
    else:
        print("NO")
