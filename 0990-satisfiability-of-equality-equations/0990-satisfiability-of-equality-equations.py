class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {
            "a":"a","b":"b","c":"c","d":"d","e":"e","f":"f","g":"g","h":"h","i":"i","j":"j","k":"k","l":"l","m":"m","n":"n","o":"o","p":"p","q":"q","r":"r","s":"s","t":"t","u":"u","v":"v","w":"w","x":"x","y":"y","z":"z"
        }
        rank = [0 for i in range(26)]

        def find(x):
            if x == parent[x]:
                return x
            while x != parent[x]:
                x = parent[x]
            return x
        def union(x,y):
            rep_x = parent[x]
            rep_y = parent[y]
            ind1 = ord(rep_x) - ord("a")
            ind2 = ord(rep_y) - ord("a")
            if rep_x != rep_y:
                if rank[ind1] > rank[ind2]:
                    parent[rep_y] = rep_x
                elif rank[ind1] < rank[ind2]:
                    parent[rep_x] = rep_y
                else:
                    parent[rep_x] = rep_y
                    rank[ind2] += 1
        for i in range(len(equations)):
            a,val,b = equations[i][0],equations[i][1],equations[i][-1]
            if val == "=":
                if find(a) != find(b):
                    union(a,b)
        for i in range(len(equations)):
            a,val,b = equations[i][0],equations[i][1],equations[i][-1]
            if val == "!":
                rep_a = find(a)
                rep_b = find(b)
                if rep_a == rep_b:
                    return False
        return True

