class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def ins(l1,l2):
            i,j = 0,0
            l = []
            while i<len(l1) and j<len(l2):
                if l1[i]<=l2[j]:
                    l.append(l1[i])
                    i += 1
                else:
                    l.append(l2[j])
                    j += 1
            while i<len(l1):
                l.append(l1[i])
                i += 1
            while j< len(l2):
                l.append(l2[j])
                j += 1
            
            return l
        
        def m(left,right,arr):
            if right==left:
                return [arr[left]]

            mid = (left+right)//2
            left_element = m(left,mid,arr)
            right_element = m(mid+1,right,arr)
            ans = ins(left_element , right_element)
            return ans
        return m(0,len(nums)-1,nums)