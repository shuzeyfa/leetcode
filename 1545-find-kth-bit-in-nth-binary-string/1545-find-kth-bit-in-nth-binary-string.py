class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        
        def ret(s,n):
            if n == 1:
                return s
            n -= 1
            temp = ""
            for i in s:
                if i == "0":
                    temp += "1"
                else:
                    temp += "0"
            return ret(s + "1" + temp[::-1],n)
        s2 = ret(s,n)
        return s2[k-1]
        