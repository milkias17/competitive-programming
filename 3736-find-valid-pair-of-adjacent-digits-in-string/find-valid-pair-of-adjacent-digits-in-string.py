class Solution:
    def findValidPair(self, s: str) -> str:
        counter = Counter(s)
        left = 0
        for right in range(1, len(s)):
            left_char = s[left]
            right_char = s[right]
            if left_char != right_char and counter[left_char] == int(left_char) and counter[right_char] == int(right_char):
                return s[left] + s[right]
            left += 1
        
        return ""