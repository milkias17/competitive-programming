class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occurences = []
        windowLeft = 0
        windowRight = 0
        maxLen = 0

        while windowRight < len(s):
            if s[windowRight] not in occurences:
                occurences.append(s[windowRight])
                windowRight += 1
            else:
                maxLen = max(maxLen, windowRight - windowLeft)
                occurences.pop(0)
                windowLeft += 1

        maxLen = max(maxLen, len(occurences))
        return maxLen


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))
    print(sol.lengthOfLongestSubstring("bbbbb"))
    print(sol.lengthOfLongestSubstring("pwwkew"))
    print(sol.lengthOfLongestSubstring(" "))
