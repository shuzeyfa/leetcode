class Solution:
    def kthCharacter(self, k: int) -> str:
        s="a"
        def ret(s):
            if len(s) >= k:
                return s
            s2 = []
            for i in s:
                val1 = ord(i) + 1
                val2 = ord("a")
                val3 = val1 - val2
                val3 = val3 % 26
                val3 += val2
                s2.append(chr(val3))

            return  ret(s + "".join(s2))

        temp = ret(s)
        return temp[k-1]