class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        t=True
        for i in range(left,right+1):
            t2=False
            for j in ranges:
                if i>=j[0] and i<=j[1]:
                    t2=True
                    break
            if t2==False:
                t=False
                break
        return t
            