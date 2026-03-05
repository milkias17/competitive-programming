class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = Node(homepage)

    def visit(self, url: str) -> None:
        self.cur.next = Node(url, prev=self.cur)
        self.cur = self.cur.next

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if not self.cur.prev:
                break
            self.cur = self.cur.prev

        return self.cur.val
        

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if not self.cur.next:
                break
            self.cur = self.cur.next
        
        return self.cur.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)