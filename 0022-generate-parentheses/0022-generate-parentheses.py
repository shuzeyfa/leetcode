class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        val = []

        def back():
            if len(val) == n*2:
                copy = "".join(val)
                res.append(copy)
                return 
            
            for i in range(2):
                if i == 0:
                    val.append("(")
                else:
                    val.append(")")
                back()

                val.pop()

        back()

        def check(s):
            stack = []
            for j in s:
                if j == "(":
                    stack.append(j)
                else:
                    if stack:
                        stack.pop()
                    else:
                        return False
            return len(stack) == 0

        l = []
        for i in res:
            if check(i):
                l.append(i)
        return l