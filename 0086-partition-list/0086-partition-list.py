# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        beforenode=ListNode(0)
        afternode=ListNode(0)
        before=beforenode
        after=afternode
        cur=head
        while cur:
            if cur.val<x:
                before.next=cur
                before=before.next
            else:
                after.next=cur
                after=after.next
            cur=cur.next
        after.next=None
        before.next=afternode.next
        return beforenode.next