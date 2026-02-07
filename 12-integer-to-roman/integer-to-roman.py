class Solution:
    def _get_max(self, num, subtractive=False):
        prev = None
        arr = [1, 5, 10, 50, 100, 500, 1000]
        if subtractive:
            arr = [4, 9, 40, 90, 400, 900]

        for val in arr:
            if val <= num:
                prev = val
            else:
                break
        
        return prev

    def intToRoman(self, num: int) -> str:
        rom_numeral = []
        mapper = {
            	1: "I",
            	5: "V",
            	10: "X",
            	50: "L",
            	100: "C",
            	500: "D",
            	1000: "M",
                4: "IV",
                9: "IX",
                40: "XL",
                90: "XC",
                400: "CD",
                900: "CM"
        }
        consec = {
            "I": 0,
            "X": 0,
            "C": 0,
            "M": 0
        }
        while num > 0:
            num_str = str(num)
            if num_str[0] in ["4", "9"]:
                tmp = self._get_max(num, True)
                rom_numeral.append(mapper[tmp])
                num -= tmp
            else:
                tmp = self._get_max(num)
                if mapper[tmp] not in consec and len(rom_numeral) > 0 and rom_numeral[-1] == mapper[tmp]:
                    tmp = self._get_max(num, True)
                elif mapper[tmp] in consec and consec[mapper[tmp]] > 3:
                    tmp = self._get_max(num, True)
                    consec[mapper[tmp]] = 0
                elif mapper[tmp] in consec:
                    consec[mapper[tmp]] += 1

                
                rom_numeral.append(mapper[tmp])
                num -= tmp
            

        return "".join(rom_numeral)

