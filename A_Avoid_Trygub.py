from typing import List

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        def dfs(i):
            if i == len(cookies):  # If all cookies are assigned
                return max(kids)  # Return the maximum cookies any kid has
            
            best = float('inf')
            for j in range(k):
                kids[j] += cookies[i]  # Give cookie to kid j
                best = min(best, dfs(i + 1))  # Recur for the next cookie
                kids[j] -= cookies[i]  # Undo (backtrack)
                
                if kids[j] == 0:  # Optimization: If a kid gets their first cookie, break
                    break
            
            return best
        
        kids = [0] * k  # Track cookies for each kid
        return dfs(0)

# Example usage
cookies = [8, 15, 20, 10, 8]
k = 2
print(Solution().distributeCookies(cookies, k))  # Output: 31
