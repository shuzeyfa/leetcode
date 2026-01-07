# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next==None:
            return True
        if head.next.next==None:
            if head.next.val==head.val:
                return True
            return False
        if head.next.next.next==None:
            if head.val==head.next.next.val:
                return True
            return False

        count=0
        cur=head
        while cur:
            count+=1
            cur=cur.next
        length=count
        count=count//2
        ind=0
        cur=head
        while ind<count-1:
            ind+=1
            cur=cur.next
        if length%2==0:
            sec=cur.next
        else:
            sec=cur.next.next
        prev=None
        cur=head
        ind=0
        while ind<count:
            n=cur.next
            ind+=1
            cur.next=prev
            prev=cur
            cur=n
        
        while sec!=None:
            if sec.val!=prev.val:
                return False
            sec=sec.next
            prev=prev.next
        return True
        
