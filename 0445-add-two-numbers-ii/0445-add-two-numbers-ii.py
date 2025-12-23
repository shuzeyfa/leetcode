# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        s1 = ""
        while cur1:
            s1 += str(cur1.val)
            cur1 = cur1.next

        cur2 = l2
        s2 = ""
        while cur2:
            s2 += str(cur2.val)
            cur2 = cur2.next

        final = str(int(s1)+int(s2))
        head = ListNode(0)
        temp = head
        for i in final:
            new = ListNode(int(i))
            temp.next = new
            temp = temp.next
        return head.next