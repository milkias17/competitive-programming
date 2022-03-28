class Solution:
    def romanToInt(self, s: str) -> int:
        base_symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        integer = 0
        for index, numeral in enumerate(s):
             integer = integer + base_symbols[numeral]
             if index != 0:
                if numeral == "V" and s[index - 1] == "I":
                    integer = integer - 2
                if numeral == "X" and s[index - 1] == "I":
                    integer = integer - 2
                if numeral == "L" and s[index - 1] == "X":
                    integer = integer - 20
                if numeral == "C" and s[index - 1] == "X":
                    integer = integer - 20
                if numeral == "D" and s[index - 1] == "C":
                    integer = integer - 200
                if numeral == "M" and s[index - 1] == "C":
                    integer = integer - 200
                    
        return integer
        