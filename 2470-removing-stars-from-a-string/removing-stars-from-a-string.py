class Solution:
    def removeStars(self, s: str) -> str:
        new_str = []
        for char in s:
            if char != "*":
                new_str.append(char)
            else:
                new_str.pop()
        
        return "".join(new_str)