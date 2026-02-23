class Solution:
    def reverseWords(self, s: str) -> str:
        list1=s.split()
        s2=""
        for i in range(len(list1)-1,-1,-1):
            if i!=0:
                s2=s2+list1[i]+" "
            else:
                s2=s2+list1[i]
        return s2