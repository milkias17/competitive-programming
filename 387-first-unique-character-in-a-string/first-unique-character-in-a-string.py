class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = {}
        for char in s:
            counter[char] = counter.get(char, 0) + 1
        
        for i, char in enumerate(s):
            if counter[char] == 1:
                return i
        
        return -1