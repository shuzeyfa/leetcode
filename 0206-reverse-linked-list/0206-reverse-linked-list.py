# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        position=None
        current=head
        while current != None:
            next_item=current.next
            current.next=position

            position=current
            current=next_item
        return position
