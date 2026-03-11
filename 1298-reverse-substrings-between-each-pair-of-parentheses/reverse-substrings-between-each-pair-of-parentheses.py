class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for char in s:
            if char == "(" or char.isalpha():
                stack.append(char)
                continue
            
            chars = []
            while stack and stack[-1] != "(":
                chars.append(stack.pop())
            
            stack.pop()
            stack.extend(chars)
        
        return "".join(stack)