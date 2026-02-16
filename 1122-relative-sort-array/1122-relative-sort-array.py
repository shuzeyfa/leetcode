class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        l1=[]
        l2=[]
        for i in range(len(arr1)):
            if arr1[i] in arr2:
                l1.append(arr1[i])
            else:
                l2.append(arr1[i])
        l3=sorted(l1,key=arr2.index)
        l2.sort()
        final=l3+l2
        return final