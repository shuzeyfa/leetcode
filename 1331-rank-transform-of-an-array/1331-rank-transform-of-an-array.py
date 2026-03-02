class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ar=sorted(set(arr))
        rank={}
        l=[]
        for i in range(len(ar)):
            rank[ar[i]]=i+1
        for i in range(len(arr)):
            l.append(rank[arr[i]])
            
        return l   
        