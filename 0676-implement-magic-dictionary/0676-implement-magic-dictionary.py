class MagicDictionary:

    def __init__(self):
        self.l = []
        

    def buildDict(self, dictionary: List[str]) -> None:
        for i in dictionary:
            self.l.append(i)
        return
        

    def search(self, searchWord: str) -> bool:
        for i in self.l:
            if len(i) != len(searchWord):
                continue
            odd = 0
            for j in range(len(searchWord)):
                if searchWord[j] != i[j]:
                    odd += 1
                
            if odd == 1:
                return True
        return False
            
        

        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)