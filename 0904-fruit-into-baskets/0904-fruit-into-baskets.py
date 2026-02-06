class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left, right=0,0
        maxx=0
        c=Counter()
        while right<len(fruits):
            c[fruits[right]]+=1
            if len(c)<=2:
                maxx=max(maxx,(right-left)+1)
                right+=1
            else:
                right+=1
                while len(c)>2:
                    c[fruits[left]]-=1
                    if c[fruits[left]]==0:
                        c.pop(fruits[left])
                    left+=1
                
        return (maxx)