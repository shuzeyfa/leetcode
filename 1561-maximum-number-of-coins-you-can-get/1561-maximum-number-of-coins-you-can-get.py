class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        maxx=0
        index=0
        piles.sort()
        final=piles[(len(piles)//3):]
        while index<len(final):
            maxx+=(final[index])
            index+=2
        return (maxx)