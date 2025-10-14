class TrieNode():

    def __init__(self):
        self.is_end = False
        self.children = [None for i in range(26)]

class Trie:

    def __init__(self):
        self.root = TrieNode()

        
    def insert(self, word: str) -> None:
        cur = self.root
        for i in word:
            ind = ord(i) - ord("a")
            if cur.children[ind] == None:
                cur.children[ind] = TrieNode()
            cur = cur.children[ind]
        cur.is_end = True
        return
        

    def search(self, word: str) -> bool:
        cur = self.root
        for i in word:
            ind = ord(i) - ord("a")
            if cur.children[ind] == None:
                return False
            cur = cur.children[ind]
        return cur.is_end == True

        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in prefix:
            ind = ord(i) - ord("a")
            if cur.children[ind] == None:
                return False
            cur = cur.children[ind]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)