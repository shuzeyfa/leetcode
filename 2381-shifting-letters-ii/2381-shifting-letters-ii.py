class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        dp=[0]*(len(s)+1)
        for i in shifts:
            start, end, dir= i
            if dir==0:
                dp[start]-=1
                dp[end+1]+=1
            else:
                dp[start]+=1
                dp[end+1]-=1
        prefix_sum = 0
        s = list(s)  
        for i in range(len(s)):
            prefix_sum += dp[i]
            current_pos = ord(s[i]) - ord('a')
            new_pos = (current_pos + prefix_sum % 26 + 26) % 26
            s[i] = chr(ord('a') + new_pos)
        return ("".join(s))