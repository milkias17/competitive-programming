class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ref = Counter(p)

        left = 0
        cur_counter = {}
        anagrams = []
        for right in range(len(s)):
            cur_counter[s[right]] = cur_counter.get(s[right], 0) + 1
            if right - left + 1 == len(p):
                for k, v in ref.items():
                    if k not in cur_counter:
                        break
                    if v != cur_counter[k]:
                        break
                else:
                    anagrams.append(left)
                
                cur_counter[s[left]] -= 1
                left += 1
        
        return anagrams
