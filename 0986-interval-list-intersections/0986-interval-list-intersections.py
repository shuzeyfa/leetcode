class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res=[]
        left, right=0,0
        while left<len(firstList) and right<len(secondList):
            if firstList[left][1]>=secondList[right][0] and firstList[left][0]<=secondList[right][1]:
                res.append([max(secondList[right][0],firstList[left][0]),min(firstList[left][1],secondList[right][1])])
            if firstList[left][1]<=secondList[right][1]:
                left+=1
            else:
                right+=1
        return res