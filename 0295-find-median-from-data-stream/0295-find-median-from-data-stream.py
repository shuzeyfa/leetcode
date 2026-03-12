class MedianFinder:

    def __init__(self):
        self.heap1 = []
        self.heap2 = []
        

    def addNum(self, num: int) -> None:
        if len(self.heap2) < len(self.heap1) + 1:
            minn = float("inf")
            if len(self.heap1) > 0:
                minn = -heappop(self.heap1)
            if minn != float("inf"):
                if minn > num:
                    heappush(self.heap2,minn)
                    heappush(self.heap1,-num)
                else:
                    heappush(self.heap2,num)
                    heappush(self.heap1,-minn)
            else:
                heappush(self.heap2,num)
        else:
            minn = heappop(self.heap2)
            if num > minn:
                heappush(self.heap2,num)
                heappush(self.heap1,-minn)
            else:
                heappush(self.heap2,minn)
                heappush(self.heap1,-num)
        

    def findMedian(self) -> float:
        if (len(self.heap1) + len(self.heap2)) % 2 == 1:
            minn = heappop(self.heap2)
            heappush(self.heap2,minn)
            return minn
        else:
            left, right = -heappop(self.heap1), heappop(self.heap2)
            heappush(self.heap2,right)
            heappush(self.heap1,-left)
            return (left + right) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()