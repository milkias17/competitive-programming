class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        longest_substr = ""
        prev_encountered = {s[0]: 0}
        left = 0
        for right in range(1, len(s)):
            char = s[right]
            prev = prev_encountered.get(char, -1)
            if prev >= left:
                left = prev + 1
            
            if right - left + 1 > len(longest_substr):
                longest_substr = s[left:right + 1]
            
            prev_encountered[char] = right
        
        return len(longest_substr)