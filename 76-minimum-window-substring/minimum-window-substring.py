class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cur_counter = Counter()
        t_counter = Counter(t)

        def is_valid():
            for char, count in t_counter.items():
                if char not in cur_counter or cur_counter[char] < count:
                    return False
                

            return True
        
        left = 0
        ans = None

        for right in range(len(s)):
            cur_counter[s[right]] += 1

            while is_valid():
                if ans is None or len(ans) > right - left + 1:
                    ans = s[left:right + 1]
                cur_counter[s[left]] -= 1
                left += 1
        
        return ans if ans is not None else ""
            
