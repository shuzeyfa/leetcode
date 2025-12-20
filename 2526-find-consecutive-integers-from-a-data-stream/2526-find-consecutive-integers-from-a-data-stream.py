class DataStream:

    def __init__(self, value: int, k: int):
        self.q = deque()
        self.c = 0
        self.length = 0
        self.val = value
        self.k2 = k
        

    def consec(self, num: int) -> bool:
        self.q.append(num)
        self.length += 1
        if num == self.val:
            self.c += 1
        while self.length>self.k2:
            temp = self.q.popleft()
            self.length -= 1
            if temp == self.val:
                self.c -= 1
        return True if self.c == self.k2 else False
        
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)