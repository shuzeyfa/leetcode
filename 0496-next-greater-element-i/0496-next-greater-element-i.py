class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}

        l = []
        for i in nums2:
            if len(l)<=0:
                l.append(i)
            else:
                if l[-1] >= i:
                    l.append(i)
                else:
                    while len(l)>0 and l[-1] < i:
                        d[l.pop()] = i
                    l.append(i)

        l2 = []
        for i in nums1:
            if i in d:
                l2.append(d[i])
            else:
                l2.append(-1)
        return l2



