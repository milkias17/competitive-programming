class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ref_counter = {}
        for char in p:
            ref_counter[char] = ref_counter.get(char, 0) + 1
        
        cur_counter = {}
        left = 0
        right = 0
        out = []
        while right < len(s):
            if s[right] not in ref_counter:
                left = right + 1
                right = left
                cur_counter = {}
                continue
            
            cur_counter[s[right]] = cur_counter.get(s[right], 0) + 1
            
            if right - left + 1 == len(p):
                valid = True
                for char, count in ref_counter.items():
                    if cur_counter.get(char, 0) != count:
                        valid = False
                        break
                
                if valid:
                    out.append(left)
                
                cur_counter[s[left]] -= 1
                if cur_counter[s[left]] == 0:
                    del cur_counter[s[left]]
                left += 1
                right += 1
            else:
                right += 1
        
        return out


