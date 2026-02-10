class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new_str = [None] * len(s)

        for i,idx in enumerate(indices):
            new_str[idx] = s[i]
        
        return "".join(new_str)