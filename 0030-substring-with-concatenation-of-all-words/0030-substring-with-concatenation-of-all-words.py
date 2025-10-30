class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        total = len(words)*len(words[0])
        word_len = len(words[0])

        check = Counter(words)

        ans = []
        
        for i in range(0, len(s) - total + 1):
            partition = s[i: i+total]
            seen = Counter()
            for j in range(0, total, word_len):
                val = partition[j: j + word_len]
                seen[val] += 1
            
            if seen == check:
                ans.append(i)
        return ans
