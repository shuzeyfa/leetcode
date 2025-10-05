class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        @lru_cache(None)

        def dp(sind, tind):
            if tind == len(t):
                return 1
            
            if sind >= len(s):
                return 0
            
            include = 0
            if s[sind] == t[tind]:
                include += dp(sind+1, tind+1)
            # else:
            #     include += dp(sind+1, tind)
            exclude = dp(sind+1, tind)
            return exclude + include
        
        return dp(0, 0)