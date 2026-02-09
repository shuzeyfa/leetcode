class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c==1 or c==0:
            return True
        l=[x for x in range((int(sqrt(c)))+1)] 
        left, right = 0, len(l)-1
        while left<=right:
            if (l[left]*l[left])+(l[right]*l[right])==c:
                return True
            elif (l[left]*l[left])+(l[right]*l[right])>c:
                right-=1
            else:
                left+=1

        return False 