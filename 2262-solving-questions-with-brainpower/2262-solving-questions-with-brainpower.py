from functools import lru_cache
import sys
sys.setrecursionlimit(1 << 20)

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        @lru_cache(None)
        def dp(ind):
            if ind >= len(questions):
                return 0
            
            return max(dp(ind+1+questions[ind][-1])+questions[ind][0], dp(ind+1))
        
        return dp(0)