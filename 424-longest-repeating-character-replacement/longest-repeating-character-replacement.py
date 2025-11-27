class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= 1:
            return len(s)

        longest = 1
        counter = {s[0]: 1}
        left = 0
        populous = s[left]
        for right in range(1, len(s)):
            total_els = right - left + 1
            counter[s[right]] = counter.get(s[right], 0) + 1
            if counter[s[right]] > counter[populous]:
                populous = s[right]
            ignored_els = total_els - counter.get(populous, 0)

            while ignored_els > k:
                counter[s[left]] -= 1
                left += 1
                total_els -= 1
                populous = max(counter, key=counter.get)
                ignored_els = total_els - counter.get(populous, 0)
            
            longest = max(longest, total_els)
        
        return longest