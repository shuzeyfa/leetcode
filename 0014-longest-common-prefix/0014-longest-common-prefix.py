class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        res=strs[0]
        for word in strs[1:]:
            temp=""
            for i in range(min(len(res),len(word))):
                if res[i]==word[i]:
                    temp+=res[i]
                else:
                    break
            res=temp
        return res            