class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        deg = [0]*len(quiet)
        d = defaultdict(list)
        for u,v in richer:
            deg[v] += 1
            d[u].append(v)
        g = [set() for i in range(len(quiet))]
        q = deque()
        for i in range(len(quiet)):
            if deg[i] == 0:
                q.append(i)

        while q:
            cur = q.popleft()
            for i in d[cur]:
                g[i].update(g[cur])
                g[i].add(cur)
                deg[i] -= 1
                if deg[i] == 0:
                    q.append(i)
        d2 = defaultdict()
        for i in range(len(quiet)):
            d2[i] = quiet[i]
        ans = []
        for i in range(len(quiet)):
            minn = float("inf")
            val = i
            for j in g[i]:
                if d2[j] < minn:
                    val = j
                    minn = d2[j]
            if minn < d2[i]:
                ans.append(val)
            else:
                ans.append(i)

        return ans
