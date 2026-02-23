class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left = 0
        for right in range(len(haystack)):
            if right - left + 1 == len(needle) :
                if haystack[left:right+1] == needle:
                    return left
                left += 1
        
        return -1
