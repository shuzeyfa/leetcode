class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s2 = []
        t2 = []
        for i in s:
            if i == "#":
                if s2:
                    s2.pop()
            else:
                s2.append(i)

        for i in t:
            if i == "#":
                if t2:
                    t2.pop()
            else:
                t2.append(i)
        return "".join(s2) == "".join(t2)