class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]
        self.value = 0




class MapSum:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, key: str, val: int) -> None:
        cur = self.root

        for i in key:
            ind = ord(i) - ord("a")
            if cur.children[ind] == None:
                cur.children[ind] = TrieNode()
            cur = cur.children[ind]
        cur.value = val
        

        

    def sum(self, prefix: str) -> int:

        cur = self.root

        for i in prefix:
            ind = ord(i) - ord("a")
            if cur.children[ind] == None:
                return 0
            cur = cur.children[ind]
        
        ans = 0
        stack = [cur]
        while stack:
            cur = stack.pop()
            ans += cur.value
            for j in cur.children:
                if j != None:
                    stack.append(j)
        return ans


        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)