class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        list_magazine = list(magazine)
        for letter in ransomNote:
            try:
                index = list_magazine.index(letter)
                list_magazine.pop(index)
            except:
                return False
        return True
        