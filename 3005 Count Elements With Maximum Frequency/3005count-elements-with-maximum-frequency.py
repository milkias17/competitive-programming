class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = {}
        max_freq = -1
        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1
            max_freq = max(max_freq, counter[num])
        
        total = 0
        for val in counter.values():
            if val == max_freq:
                total += val

        return total