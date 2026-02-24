class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        chars = set()
        left = 0
        res = []
        for right in range(len(s)):
            chars.add(s[right])
            flag = True
            for char in chars:
                if char in s[right + 1:]:
                    flag = False
                    break
            
            if flag:
                res.append(right - left + 1)
                chars.clear()
                left = right + 1
        
        return res

