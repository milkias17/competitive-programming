class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(magazine)
        for char in ransomNote:
            if char not in counter or counter[char] <= 0:
                return False
            counter[char] -= 1
        
        return True