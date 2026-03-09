class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapper = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for char in s:
            if char not in mapper:
                stack.append(char)
            else:
                if len(stack) == 0 or stack[-1] != mapper[char]:
                    return False
                stack.pop()
        
        return len(stack) == 0
