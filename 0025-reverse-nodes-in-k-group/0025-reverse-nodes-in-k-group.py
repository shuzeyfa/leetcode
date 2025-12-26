# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==1:
            return head
        c = head
        n=0
        while c:
            n += 1
            c = c.next
        l=[]
        cur = head
        for i in range(n//k):
            ind = k
            temp = []
            while ind>0:
                temp.append(cur.val)
                cur = cur.next
                ind-=1
            l.append(temp)
        
        dummy = ListNode(0)
        cur2 = dummy

        for i in l:
            for j in range(len(i)-1,-1,-1):
                new = ListNode(i[j])
                cur2.next = new
                cur2 = cur2.next
        while cur:
            cur2.next = cur
            cur = cur.next
            cur2 = cur2.next
        return dummy.next
