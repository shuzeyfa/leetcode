class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        @lru_cache(None)
        def dp(sind, tind):
            if sind == len(s):
                return True
            
            if tind >= len(t):
                return False
            
            if s[sind] == t[tind]:
                return dp(sind+1, tind+1)
            else:
                return dp(sind, tind+1)
        
        return dp(0, 0)