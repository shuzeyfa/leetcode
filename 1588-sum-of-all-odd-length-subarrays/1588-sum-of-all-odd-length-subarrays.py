class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        maxx=0
        for i in range(1,len(arr)+1,2):
            l,r=0,i-1
            summ=sum(arr[l:r+1])
            while r<len(arr):
                maxx+=summ
                r+=1
                if r<len(arr):
                    summ+=arr[r]
                summ-=arr[l]
                l+=1
        return maxx