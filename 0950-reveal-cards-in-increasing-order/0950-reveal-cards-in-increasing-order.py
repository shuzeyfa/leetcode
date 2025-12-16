class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        de = deque()
        deck.sort(reverse = True)
        for i in deck:
            if len(de)>0:
                k = de.pop()
                de.appendleft(k)
            de.appendleft(i)
        return list(de)
