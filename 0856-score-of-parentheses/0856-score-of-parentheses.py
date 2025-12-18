class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        tot = 0
        l = [0]
        for i in s:
            if i == "(":
                l.append(0)
            else:
                top = l.pop()
                l[-1] += (max(top*2,1))

        return l[-1]
        