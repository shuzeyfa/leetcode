class TrieNode():

    def __init__(self):
        self.is_end = False
        self.children = [None for i in range(26)]

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # your code goes here  
        cur = self.root
        for i in word:
            ind = ord(i) - ord("a")
            if cur.children[ind] == None:
                cur.children[ind] = TrieNode()
            cur = cur.children[ind]
        cur.is_end = True
        return

class Solution:
    def longestWord(self, words: List[str]) -> str:

        trie = Trie()

        l = [""]
        for i in words:
            trie.insert(i)
        
        maxx = 0

        for i in words:
            cur = trie.root
            temp = []
            valid = True
            for j in i:
                ind = ord(j) - ord("a")
                if  cur.children[ind] == None or not cur.children[ind].is_end:
                    value = False
                    break
                temp.append(j)
                cur = cur.children[ind]
            val = "".join(temp)
            if valid and len(val) > maxx:
                maxx = len(val)
                l = [val]  # Reset list to current candidate
            elif valid and len(val) == maxx and val < l[0]:
                l = [val]  # Update to lexicographically smaller candidate

        return l[0] if l else ""




        
