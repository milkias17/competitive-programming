class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for char in s:
            if char.isnumeric():
                stack.pop()
            else:
                stack.append(char)
        
        return "".join(stack)