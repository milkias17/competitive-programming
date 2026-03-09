class Solution:
    def check_valid(self, s_counter, t_counter):
        for k, v in t_counter.items():
            if k not in s_counter or s_counter[k] < v:
                return False
        
        return True

    def minWindow(self, s: str, t: str) -> str:
        org_counter = Counter(t)
        counter = Counter()
        left = 0
        min_subs = ""
        min_length = float("inf")
        for right in range(len(s)):
            if s[right] in org_counter:
                counter[s[right]] += 1
                if counter[s[right]] == 0:
                    del counter[s[right]]
            
            while self.check_valid(counter, org_counter):
                # print(f"In for: {s[left:right+1]}, counter: {counter}")
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_subs = s[left:right+1]
                
                if s[left] in counter:
                    counter[s[left]] -= 1
                left += 1

        return min_subs
                
                
