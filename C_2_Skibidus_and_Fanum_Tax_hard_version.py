import sys
sys.setrecursionlimit(10**6)

def solve():
    n, m = map(int, input().split())
    s = input().strip()
    
    # Graph
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)  # zero-based indexing
    
    # DP table: dp[node][char] = maximum count of char on any path ending at node
    dp = [[0] * 26 for _ in range(n)]
    

    visited = [0] * n  # 0 = unvisited, 1 = visiting, 2 = visited
    ans = 0
    has_cycle = [False]

    def dfs(u):
        visited[u] = 1  # currently visiting
        idx = ord(s[u]) - ord('a')
        dp[u][idx] = 1  # count current node's character
        
        for v in graph[u]:
            if visited[v] == 0:
                dfs(v)
            elif visited[v] == 1:
                has_cycle[0] = True  # found a cycle
            
            for c in range(26):
                dp[u][c] = max(dp[u][c], dp[v][c] + (1 if c == idx else 0))
        
        visited[u] = 2  # finished visiting

    for i in range(n):
        if visited[i] == 0:
            dfs(i)

    if has_cycle[0]:
        print(-1)
    else:

        for i in range(n):
            ans = max(ans, max(dp[i]))
        print(ans)

# Run
solve()
