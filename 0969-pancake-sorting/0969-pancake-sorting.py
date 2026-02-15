class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        l2=copy.deepcopy(arr)
        l2.sort(reverse=True)
        l3=[]

        index=len(arr)
        for i in l2:
            temp=arr.index(i)+1
            l3.append(temp)
            temp2=arr[:temp]
            temp2.reverse()
            arr=temp2+arr[temp:]
            l3.append(index)
            temp3=arr[:index]
            temp3.reverse()
            arr=temp3+arr[index:]
            index-=1
        return (l3)