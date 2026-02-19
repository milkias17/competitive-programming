class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy_count = 0
        yx_count = 0

        for idx in range(len(s1)):
            if s1[idx] == s2[idx]:
                continue
            
            if s1[idx] == "x":
                xy_count += 1
            elif s1[idx] == "y":
                yx_count += 1
        
        if (xy_count + yx_count) % 2 != 0:
            return -1
        
        count = xy_count // 2 + yx_count // 2

        if xy_count % 2 != 0 and yx_count % 2 != 0:
            count += 2
        
        return count

