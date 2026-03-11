class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []

        for char in s:
            if char != "#":
                stack_s.append(char)
                continue
            
            if stack_s:
                stack_s.pop()

        for char in t:
            if char != "#":
                stack_t.append(char)
                continue
            
            if stack_t:
                stack_t.pop()
        

        return stack_s == stack_t
        