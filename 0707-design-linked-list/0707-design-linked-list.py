class node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = node(0)
        self.tail = node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        cur = self.head.next
        while cur != self.tail and index>0:
            cur = cur.next
            index -= 1
        if cur == self.tail:
            return -1
        return cur.val

    def addAtHead(self, val: int) -> None:
        new = node(val)
        nxt = self.head.next
        self.head.next = new
        new.prev = self.head
        new.next = nxt
        nxt.prev = new

    def addAtTail(self, val: int) -> None:
        pre = self.tail.prev

        new = node(val)
        new.next = self.tail
        self.tail.prev = new
        new.prev = pre
        pre.next = new
        

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.head.next
        while cur!=self.tail and index>0:
            cur = cur.next
            index -= 1
        if index>0:
            return 
        if cur == self.tail:
            pre = self.tail.prev
            new = node(val)
            new.next = self.tail
            self.tail.prev = new
            new.prev = pre
            pre.next = new
            return 
        pre = cur.prev
        new = node(val)
        pre.next = new
        new.prev = pre
        new.next = cur
        cur.prev = new


    def deleteAtIndex(self, index: int) -> None:
        cur = self.head.next
        while cur!= self.tail and index>0:
            cur = cur.next
            index -= 1
        if index>0 or cur == self.tail:
            return 
        pre = cur.prev
        nxt = cur.next
        pre.next = nxt
        nxt.prev = pre
        return 


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)