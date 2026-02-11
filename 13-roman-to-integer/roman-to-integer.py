class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        i = 0
        mapper = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        while i < len(s):
            char = s[i]
            if char == "I" and i + 1 < len(s) and s[i + 1] in ["V", "X"]:
                num += mapper[s[i + 1]] - mapper[char]
                i += 2
            elif char == "X" and i + 1 < len(s) and s[i + 1] in ["L", "C"]:
                num += mapper[s[i + 1]] - mapper[char]
                i += 2
            elif char == "C" and i + 1 < len(s) and s[i + 1] in ["D", "M"]:
                num += mapper[s[i + 1]] - mapper[char]
                i += 2
            else:
                num += mapper[char]
                i += 1
            

        return num
