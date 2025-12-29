# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = ""
        second = ""

        cur = l1
        while cur:
            temp = cur.val
            first += str(temp)
            cur = cur.next

        cur2 = l2
        while cur2:
            temp2 = cur2.val
            second += str(temp2)
            cur2 = cur2.next
            
        final = int(first[::-1]) + int(second[::-1])
        l=list(str(final))

        final_2 = str(final)[::-1]
        l3=list(final_2)
        
        dummy = ListNode(0)
        new = ListNode(int(l3[0]))
        dummy.next = new 
        cur = dummy.next
        for i in range(1,len(l3)):
            new2 = ListNode(int(l3[i]))
            cur.next = new2
            cur = cur.next
        return dummy.next
