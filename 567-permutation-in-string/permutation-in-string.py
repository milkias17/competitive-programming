from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ref_counter = Counter(s1)

        cur_counter = {}
        left = 0
        right = 0
        while right < len(s2):
            if s2[right] not in ref_counter:
                left = right + 1
                right = left
                cur_counter = {}
                continue
            
            cur_counter[s2[right]] = cur_counter.get(s2[right], 0) + 1
            if right - left + 1 == len(s1):
                valid = True
                for char, count in ref_counter.items():
                    if cur_counter.get(char, 0) != count:
                        valid = False
                        break
                
                if valid:
                    return True
                
                cur_counter[s2[left]] -= 1
                if cur_counter[s2[left]] == 0:
                    del cur_counter[s2[left]]
                left += 1
                right += 1
            else:
                right += 1
    
        return False
