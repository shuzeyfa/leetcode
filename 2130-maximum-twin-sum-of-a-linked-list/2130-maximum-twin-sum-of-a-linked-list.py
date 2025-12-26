# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        while fast:
            slow = slow.next
            fast = fast.next.next
        cur = slow
        prev = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        tot = 0
        cur2 = head
        while prev:
            temp = prev.val + cur2.val
            if temp>tot:
                tot = temp
            prev = prev.next
            cur2 = cur2.next
        return tot