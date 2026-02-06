class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heappush_max(self.small, num)
        if self.small and self.large and self.small[0] > self.large[0]:
            val = heappop_max(self.small)
            heappush(self.large, val)
        
        if len(self.small) > len(self.large) + 1:
            val = heappop_max(self.small)
            heappush(self.large, val)
        elif len(self.large) > len(self.small) + 1:
            val = heappop(self.large)
            heappush_max(self.small, val)
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        
        val1 = self.small[0]
        val2 = self.large[0]
        return (val1 + val2) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()