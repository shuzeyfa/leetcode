class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        parent = {i:i for i in range(len(strs))}
        rank = [0]*(len(strs))
        
        def valid(str1, str2):
            count = 0
            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    count += 1
                if count > 2:
                    return False
            return True
        def find(x):
            if x == parent[x]:
                return x
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(left, right):
            rep1, rep2 = find(left), find(right)
            if rep1 != rep2:
                if rank[rep1] > rank[rep2]:
                    parent[rep2] = rep1
                elif rank[rep2] > rank[rep1]:
                    parent[rep1] = rep2
                else:
                    parent[rep2] = rep1
                    rank[rep1] += 1


        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                if valid(strs[i], strs[j]):
                    union(i,j)
        s = set()
        for i in range(len(strs)):
            val = find(i)
            s.add(val)
        return len(s)