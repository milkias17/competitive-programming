class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        counter = {}
        cur_sequence = ""
        left = 0
        for right in range(len(s)):
            cur_sequence += s[right]
            if right - left + 1 == 10:
                counter[cur_sequence] = counter.get(cur_sequence, 0) + 1
                cur_sequence = cur_sequence[1:]
                left += 1
        
        return [k for k, v in counter.items() if v > 1]
