class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter_s = Counter(s)
        counter_t = Counter(t)

        needed = 0
        for char, count in counter_s.items():
            if char not in counter_t:
                needed += count
            elif counter_t[char] < count:
                needed += abs(count - counter_t[char])
        
        return needed
        