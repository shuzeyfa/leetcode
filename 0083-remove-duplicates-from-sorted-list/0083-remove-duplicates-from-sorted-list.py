# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        dummy=cur
        while cur:
            temp=cur.next
            while temp!=None and temp.val==cur.val:
                temp=temp.next
            cur.next=temp
            cur=cur.next
        return dummy
