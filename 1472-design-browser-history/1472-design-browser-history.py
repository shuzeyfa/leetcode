class node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head=node(0)
        self.tail=node(0)
        new = node(homepage)
        self.head.next = new
        new.prev = self.head
        new.next = self.tail
        self.tail.prev = new

        self.cur=self.head.next

    def visit(self, url: str) -> None:
        new1 = node(url)

        self.cur.next=new1
        new1.prev=self.cur
        new1.next=self.tail
        self.tail.prev=new1
        self.cur=self.cur.next

        

    def back(self, steps: int) -> str:
        while self.cur.prev !=self.head and steps>0:
            self.cur=self.cur.prev
            steps-=1
        return self.cur.val

    def forward(self, steps: int) -> str:
        while self.cur.next != self.tail and steps>0:
            self.cur=self.cur.next
            steps-=1
        return self.cur.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)