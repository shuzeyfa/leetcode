class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        d = defaultdict(int)

        for i in range(lo, hi+1):

            count = 0
            key = i

            while key != 1:
                count += 1
                if key%2 == 0:
                    key //= 2
                else:
                    key = 3*key + 1
                
            d[i] = count
        
        ans = list(sorted(d.items(), key=lambda x:x[1]))
        # print()
        # print(ans)
        key, val = ans[k-1]
        return key
