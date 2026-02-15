class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        count=len(citations)
        for i in range(len(citations)):
            if citations[i]<i+1:
                count=i
                break
        return count
                