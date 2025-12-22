class Solution:
    def simplifyPath(self, path: str) -> str:
        s = list(path.split("/"))
        l = []
        for i in s:
            if i == "" or i == ".":
                continue
            elif i == "..":
                if len(l)>0:
                    l.pop()
                
            else:
                l.append(i)
        final = "/"
        for i in l:
            final += i
            final += "/"
        return final[:len(final)-1] if len(l)>0 else "/"