class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        parent = {i:i for i in range(len(accounts))}
        rank = [0 for i in range(len(accounts))]
        def find(x):
            if x == parent[x]:
                return x
            while x != parent[x]:
                x = parent[x]
            return x

        def union(x,y):
            rep_y = find(y)
            rep_x = find(x)
            if rep_x != rep_y:
                if rank[rep_x] > rank[rep_y]:
                    parent[rep_y] = rep_x
                elif rank[rep_x] < rank[rep_y]:
                    parent[rep_x] = rep_y
                else:
                    parent[rep_y] = rep_x
                    rank[rep_x] += 1
        
        for i in range(len(accounts)):
            for j in range(len(accounts)):
                if i != j:
                    first,sec = set(accounts[i][1:]), set(accounts[j][1:])
                    
                    s = set()
                    s.update(first)
                    s.update(sec)

                    if len(s) < len(first)+len(sec):
                        union(i,j)
        d = defaultdict(list)
        for i in range(len(accounts)):
            rep = find(i)
            d[rep].append(i)
        # print(d)
        ans = []
        for i in d:
            s = set()
            l = [accounts[i][0]]
            for j in d[i]:
                s.update(set(accounts[j][1:]))
            l2 = list(s)
            l2.sort()
            l.extend(l2)
            ans.append(l)
        return ans