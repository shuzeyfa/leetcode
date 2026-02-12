class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=[]
        left= right= maxx=0
        while right<len(s):
            if s[right] not in l:
                l.append(s[right])
                right+=1
                maxx=max(maxx,right-left)
            else:
                while left<len(s) and l[0]!=s[right]:
                    l.pop(0)
                    left+=1
                l.pop(0)
                left+=1
                l.append(s[right])
                right+=1
            maxx=max(maxx,right-left)
        return (maxx)