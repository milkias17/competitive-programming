class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        desc_g = sorted(g, reverse=True)
        desc_s = sorted(s, reverse=True)
        count = 0
        cur_s = 0
        for i, child_greed in enumerate(desc_g):
            if cur_s >= len(desc_s):
                break
            if desc_s[cur_s] >= child_greed:
                count += 1
                cur_s += 1
               
        
        return count
