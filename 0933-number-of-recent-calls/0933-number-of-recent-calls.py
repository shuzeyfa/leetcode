class RecentCounter:

    def __init__(self):
        self.req = 0
        self.l=[]
        

    def ping(self, t: int) -> int:
        self.l.append(t)
        re = 0
        left = t - 3000
        right = t
        for i in self.l:
            if i>=left and i<=right:
                re += 1

        return re

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)