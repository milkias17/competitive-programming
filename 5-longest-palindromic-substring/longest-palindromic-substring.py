class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = float("-inf")
        res = None

        for i, char in enumerate(s):
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            left += 1
            right -= 1
            if right - left + 1 > max_len:
                max_len = right - left + 1
                res = s[left:right + 1]
            

            left = i - 1
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            left += 1
            right -= 1
            if right - left + 1 > max_len:
                max_len = right - left + 1
                res = s[left:right + 1]
            
            
        
        return res
            