class MyCircularDeque:

    def __init__(self, k: int):
        self.de = deque()
        self.val = k
        

    def insertFront(self, value: int) -> bool:
        if self.val <= 0:
            return False
        self.de.appendleft(value)
        self.val -= 1
        return True

        

    def insertLast(self, value: int) -> bool:
        if self.val <= 0:
            return False
        self.de.append(value)
        self.val -= 1
        return True
        

    def deleteFront(self) -> bool:
        if not self.de:
            return False
        self.de.popleft()
        self.val += 1
        return True
        

    def deleteLast(self) -> bool:
        if not self.de:
            return False
        self.de.pop()
        self.val += 1
        return True
        

    def getFront(self) -> int:
        if not self.de:
            return -1
        return self.de[0]
        

    def getRear(self) -> int:
        if not self.de:
            return -1
        return self.de[-1]
        

    def isEmpty(self) -> bool:
        return len(self.de) == 0
        

    def isFull(self) -> bool:
        return self.val == 0
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()