class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0] * len(s)
        for start, end, direction in shifts:
            d = -1 if direction == 0 else 1
            prefix[start] += d
            if end + 1 < len(s):
                prefix[end + 1] += -1 * d
        
        cur = 0
        for i, num in enumerate(prefix):
            cur += num
            prefix[i] = cur

        new_str = []
        for i, char in enumerate(s):
            cur = ord(char) - ord('a')
            tmp = (cur + prefix[i]) % 26
            new_str.append(chr(tmp + ord('a')))
        
        return "".join(new_str)

