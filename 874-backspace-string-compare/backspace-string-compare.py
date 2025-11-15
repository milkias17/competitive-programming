class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []
        for char in s:
            if char == "#":
                if len(stack_s) == 0:
                    continue
                else:
                    stack_s.pop()
            else:
                stack_s.append(char)
        for char in t:
            if char == "#":
                if len(stack_t) == 0:
                    continue
                else:
                    stack_t.pop()
            else:
                stack_t.append(char)

        str_s = str(stack_s)
        str_t = str(stack_t)
        return str_s == str_t