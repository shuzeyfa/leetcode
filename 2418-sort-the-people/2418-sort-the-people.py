class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(names)):
            temp=i
            if i!=0:
                for j in range(i-1,-1,-1):
                    if heights[temp]>heights[j]:
                        heights[temp],heights[j]=heights[j],heights[temp]
                        names[temp],names[j]=names[j],names[temp]
                        temp-=1
                    else:
                        break

        return names            
