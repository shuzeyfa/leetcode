import sys, threading
input = lambda: sys.stdin.readline().strip()


n, m = map(int,input().split())
s = input()
graph = [[] for i in range(n)]
for i in range(m):
    u,v = map(int,input().split())
    graph[u-1].append(v-1)

visit = [0]*n
dp = [[0]*26 for i in range(n)]
has_ = [False]
def dfs(u):
    visit[u] = 1
    idx = ord(s[u]) - ord("a")
    dp[u][idx] = 1

    for v in graph[u]:
        if visit[v] == 1:
            has_[0] = True
        elif visit[v] == 0:
            dfs(v)
        
        for c in range(26):
            dp[u][c] = max(dp[u][c], dp[v][c] + (1 if c==idx else 0))
    visit[u] = 2

for i in range(n):
    if visit[i] == 0:
        dfs(i)

if has_[0]:
    print(-1)
else:
    ans = 0
    for i in range(n):
        ans = max(ans , max(dp[i]))
    print(ans)