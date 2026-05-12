class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        

    def addNum(self, num: int) -> None:
        if len(self.left) == 0 or num < self.left[0]:
            heappush_max(self.left, num)
        else:
            heappush(self.right, num)
        
        if len(self.left) > len(self.right) + 1:
            tmp = heappop_max(self.left)
            heappush(self.right, tmp)
        elif len(self.right) > len(self.left) + 1:
            tmp = heappop(self.right)
            heappush_max(self.left, tmp)

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return self.left[0]
        elif len(self.right) > len(self.left):
            return self.right[0]
        
        return (self.left[0] + self.right[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()