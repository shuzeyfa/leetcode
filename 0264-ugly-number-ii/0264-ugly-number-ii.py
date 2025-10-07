class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        two = three = five = 0

        ans = [1]
        while len(ans) < n:
            val1 = ans[two]*2
            val2 = ans[three]*3
            val3 = ans[five]*5
            nextval = min(val1, val2, val3)
            ans.append(nextval)

            if nextval == val1:
                two += 1
            if nextval == val2:
                three += 1
            if nextval == val3:
                five += 1
            
            

        print(ans)
            
        return ans[n-1]