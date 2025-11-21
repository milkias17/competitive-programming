class Solution:
    def frequencySort(self, s: str) -> str:
        counter = {}
        for char in s:
            counter[char] = counter.get(char, 0) + 1
        
        return "".join(sorted(s, key=lambda char: (counter[char], char), reverse=True))