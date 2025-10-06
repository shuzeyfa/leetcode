class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        d = defaultdict(int)
        for i in arr:
            d[i%k] += 1
        
        for i in d:
            if i == 0:
                continue
            rem = k - i
            if rem == i:
                if d[rem]%2 != 0:
                    return False
                continue
            if d[rem] != d[i]:
                return False
        return True