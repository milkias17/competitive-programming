"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
"""


class Solution:
    def checkValid(self, s: list) -> bool:
        if not s:
            return True

        mapper = {"(": ")", "{": "}", "[": "]"}
        first_closes = 0
        while first_closes < len(s) and s[first_closes] in mapper:
            first_closes += 1

        if first_closes == 0 or first_closes >= len(s):
            return False

        if mapper[s[first_closes - 1]] != s[first_closes]:
            return False

        s.pop(first_closes - 1)
        s.pop(first_closes - 1)

        return self.checkValid(s)

    def isValid(self, s: str) -> bool:
        return self.checkValid(list(s))


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("([)]"))
    print(sol.isValid("(())"))
