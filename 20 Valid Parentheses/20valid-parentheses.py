class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapper = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        closers = mapper.keys()
        for char in s:
            if char in closers:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if last != mapper.get(char):
                    return False
            else:
                stack.append(char)
        
        return len(stack) == 0