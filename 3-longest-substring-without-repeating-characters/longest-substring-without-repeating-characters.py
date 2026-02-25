class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        holder = set()
        left = 0
        max_len = float("-inf")
        for right in range(len(s)):
            while s[right] in holder:
                holder.remove(s[left])
                left += 1

            holder.add(s[right])
            max_len = max(max_len, right - left + 1)
        
        return max_len if max_len != float("-inf") else 0