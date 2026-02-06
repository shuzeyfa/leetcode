class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def check(s_counter,t_counter):
            for i in t_counter:
                if s_counter[i] < t_counter[i]:
                    return False
            return True
        
        left, right= 0, 0
        c1=Counter()
        c2=Counter(t)
        length= float("inf")
        final="0"
        while right<len(s):
            c1[s[right]]+=1

            while check(c1,c2):
                temp=(right-left)+1
                if temp<length:
                    length=temp
                    final=s[left:right+1]
                c1[s[left]]-=1
                left+=1
            
            right += 1
        if final=="0":
            return ""
        return final
