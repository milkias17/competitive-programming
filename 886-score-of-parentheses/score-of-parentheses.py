class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        print(s)
        if not s:
            return 0

        if len(s) == 2 and s[0] == "(" and s[1] == ")":
            return 1
        if s[0] == "(" and s[1] == ")":
            return 1 + self.scoreOfParentheses(s[2:])
        
        open_stack = ["("]
        idx = 1
        while len(open_stack) > 0:
            char = s[idx]
            if char == "(":
                open_stack.append(char)
            else:
                open_stack.pop()

            idx += 1
        

        return (2 * self.scoreOfParentheses(s[1:idx-1])) + self.scoreOfParentheses(s[idx:])
    #     total = 0
    #     open_stack = []
    #     close_stack = []
    #     cur = 0
    #     for char in s:
    #         if char == "(":
    #             open_stack.append(char)
    #             close_stack = []
    #             continue
            
    #         open_stack.pop()
    #         if len(close_stack) > 0:
    #             cur *= 2
    #         else:
    #             cur += 1
            
    #         if len(open_stack) == 0:
    #             total += cur
    #             cur = 0
    #         else:
    #             close_stack.append(char)
        
    #     return total
