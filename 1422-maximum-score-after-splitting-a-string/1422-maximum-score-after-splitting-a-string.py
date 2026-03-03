class Solution:
    def maxScore(self, s: str) -> int:
        maxx=0
        for i in range(len(s)-1):
            a=s[:i+1].count("0")
            b=s[i+1:].count("1")
            if a+b>maxx:
                maxx=a+b
        return maxx