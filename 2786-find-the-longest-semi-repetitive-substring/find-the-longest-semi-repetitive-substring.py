class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        longest = 0
        adj_start = None
        left = 0
        for right in range(1, len(s)):
            if s[right - 1] == s[right]:
                if adj_start == None:
                    adj_start = right - 1
                else:
                    left = adj_start + 1
                    adj_start = right - 1
            

            longest = max(longest, right - left + 1)
        
        return longest
