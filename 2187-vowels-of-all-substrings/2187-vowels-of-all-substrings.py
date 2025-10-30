class Solution:
    def countVowels(self, word: str) -> int:
        
        ans = 0

        for i in range(len(word)):
            if word[i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" or word[i] == "u":
                left, right = i+1, len(word) - i
                val = (left*right) 
                ans += val
        return ans