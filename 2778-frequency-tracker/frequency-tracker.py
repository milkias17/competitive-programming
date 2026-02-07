class FrequencyTracker:

    def __init__(self):
        self.freq_nums_map = defaultdict(lambda: 0)
        self.nums_freq_map = defaultdict(lambda: 0)

    def add(self, number: int) -> None:
        prev_freq = self.nums_freq_map[number]
        self.nums_freq_map[number] += 1
        if prev_freq == 0:
            self.freq_nums_map[1] += 1
        else:
            self.freq_nums_map[prev_freq] -= 1
            self.freq_nums_map[prev_freq + 1] += 1

    def deleteOne(self, number: int) -> None:
        if self.nums_freq_map[number] == 0:
            return
        
        prev_freq = self.nums_freq_map[number]
        self.nums_freq_map[number] -= 1
        self.freq_nums_map[prev_freq] -= 1
        if prev_freq - 1 > 0:
            self.freq_nums_map[prev_freq - 1] += 1
            

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq_nums_map[frequency] > 0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)