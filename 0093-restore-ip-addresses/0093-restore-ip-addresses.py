class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        ans = []
        if len(s)>12:
            return []

        def back(start, dots, char):
            if dots == 4 and start == len(s):
                ans.append(char[:-1])
                return
            if dots > 4:
                return 

            for i in range(start, min(start+3, len(s))):
                if int(s[start:i+1]) < 256 and len(str(int(s[start:i+1])))== len(s[start:i+1]):
                    back(i + 1, dots+1, char + s[start:i+1] + ".")

        back(0, 0, "")
        return ans