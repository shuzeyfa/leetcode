class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l=[x for x in range(1,n+1)]
        index=0
        while len(l)!=1:
            index+=(k-1)
            if index>=len(l):
                index=index%len(l)
            l.pop(index)
        return (l[0])