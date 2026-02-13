class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right = 0,len(numbers)-1
        l=[]
        while left!=right:
            if numbers[left]+numbers[right]==target:
                l.extend([left+1,right+1])
                return l
            elif numbers[left]+numbers[right]>target:
                right-=1
            else:
                left+=1
