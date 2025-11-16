class RecentCounter:

    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        count = 0
        self.queue.append(t)
        for time in reversed(self.queue):
            if time < t - 3000:
                break
            count += 1
        
        return count
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)